"""Clients implementation to send/read requests/responses to the device."""

import time
from typing import Union

from xaudio.communication_handlers import XAudioSerialCommHandler
from xaudio.exceptions import XAudioResponseError, XAudioTimeoutError
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    I2COverDistanceResponse,
    InfoResponse,
    NegativeResponse,
    NoDataResponse,
    RequestPacket,
    ResponsePacket,
    StatusResponse,
)

OneOfPositiveResponseMsg = Union[
    NoDataResponse, StatusResponse, InfoResponse, I2COverDistanceResponse
]


class XAudioClient:  # pylint:disable=too-few-public-methods
    """XAudio client with generic request implementation."""

    def __init__(
        self,
        port_name: str = "loop://",
        name: str = "XAudioHandler",
        timeout: int | float = 2,
    ):
        """Initialize instance.

        :param port_name: for serial (i.e. COM2)
        :param name: of communication handler for distinction
        :param timeout: time in s to wait for response

        """
        self.comm_handler = XAudioSerialCommHandler(port_name, 115200, 2, name)
        self.comm_handler.make_connection()
        self._timeout = timeout

    def request(self, data: RequestPacket) -> OneOfPositiveResponseMsg:
        """Send RequestPacket to target over communication handler and wait for response.

        :param data: to send
        :return: response msg form device

        """
        self.comm_handler.send(data.SerializeToString())

        start = time.time()
        while time.time() - start < self._timeout:
            responses = list(self.comm_handler.receive())
            if responses:
                break
        else:
            raise XAudioTimeoutError(f"No response in expected time for\n{data}")

        if len(responses) > 1:
            raise XAudioResponseError(f"Too many responses from device: {responses}")

        if responses[0] == b"":
            return NoDataResponse()

        rp = ResponsePacket.FromString(responses[0])
        msg_name = rp.WhichOneof("oneofmsg")
        if not msg_name:
            raise XAudioResponseError(
                "ResponsePacket is missing Positive or Negative msg, "
                f"packet content: {responses[0]}"
            )

        positive_response = getattr(rp, msg_name)
        if isinstance(positive_response, NegativeResponse):
            raise XAudioResponseError(
                f"Request returned negative response {positive_response}"
            )

        return getattr(positive_response, positive_response.WhichOneof("oneofmsg"))
