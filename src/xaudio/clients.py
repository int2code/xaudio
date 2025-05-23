"""Clients implementation to send/read requests/responses to the device."""

from typing import NewType, Union

from xaudio.communication_handlers import XAudioSerialCommHandler
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    I2COverDistanceResponse,
    InfoResponse,
    NegativeResponse,
    NoDataResponse,
    RequestPacket,
    ResponsePacket,
    StatusResponse,
)

OneOfPositiveResponseMsg = NewType(
    "OneOfPositiveResponseMsg",
    Union[NoDataResponse, StatusResponse, InfoResponse, I2COverDistanceResponse],
)


class XAudioClient:  # pylint:disable=too-few-public-methods
    """XAudio client with generic request implementation."""

    def __init__(self, port_name: str = "loop://", name: str = "XAudioHandler"):
        """Initialize instance.

        :param port_name: for serial (i.e. COM2)
        :param name: of communication handler for distinction

        """
        self.comm_handler = XAudioSerialCommHandler(port_name, 115200, 2, name)
        self.comm_handler.make_connection()

    def request(self, data: RequestPacket) -> OneOfPositiveResponseMsg:
        """Send RequestPacket to target over communication handler and wait for response.

        :param data: to send
        :return: response msg form device

        """
        self.comm_handler.send(data.SerializeToString())

        responses = list(self.comm_handler.receive())
        if len(responses) > 1:
            raise RuntimeError(
                f"Too many responses from device for request: {responses}"
            )

        rp = ResponsePacket.FromString(responses[0])

        msg_name = rp.WhichOneof("oneofmsg")
        if not msg_name:
            raise RuntimeError(
                "ResponsePacket is missing Positive or Negative msg, "
                f"packet content: {responses[0]}"
            )

        positive_response = getattr(rp, msg_name)
        if isinstance(positive_response, NegativeResponse):
            raise RuntimeError(
                f"Request returned negative response {positive_response}"
            )

        return getattr(positive_response, positive_response.WhichOneof("oneofmsg"))
