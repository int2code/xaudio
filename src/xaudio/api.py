"""Definition of XAudioAPI - requests that user can make to the device."""

from typing import List

from google.protobuf.internal.containers import RepeatedScalarFieldContainer

from xaudio.clients import XAudioClient
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    A2BDiscoverRequest,
    A2BMailboxAccessType,
    A2BMailboxTransferRequest,
    I2COverDistanceAccessType,
    I2COverDistanceRequest,
    I2COverDistanceResponse,
    InfoRequest,
    InfoResponse,
    NoDataResponse,
    RequestPacket,
    ResetRequest,
    StatusRequest,
    StatusResponse, A2BMailboxTransferResponse,
)


class XAudioApi:
    """XAudio available API."""

    def __init__(self, client: XAudioClient):
        self.client = client

    def info(self) -> InfoResponse:
        """Get device info.

        :return: device details like software/hardware revision or serial number

        """
        info_request = InfoRequest(dummy=True)
        request_packet = RequestPacket(info_request=info_request)
        response = self.client.request(request_packet)
        return response

    def reset(self) -> NoDataResponse:
        """Reset device - device responds before reset is performed.

        :return: confirmation of request before reset

        """
        reset_request = ResetRequest(dummy=True)
        request_packet = RequestPacket(reset_request=reset_request)
        response = self.client.request(request_packet)
        return response

    def status(self) -> StatusResponse:
        """Get device status info.

        :return: look at `StatusResponse` for more details

        """
        status_request = StatusRequest(dummy=True)
        request_packet = RequestPacket(status_request=status_request)
        response = self.client.request(request_packet)
        return response

    def a2b_discover(self) -> NoDataResponse:
        """Rediscover A2B bus.

        :return: confirmation of request

        """
        a2b_discover_request = A2BDiscoverRequest(dummy=True)
        request_packet = RequestPacket(a2b_discover_request=a2b_discover_request)
        response = self.client.request(request_packet)
        return response

    def i2c_over_distance(
        self,
        access_type: "I2COverDistanceAccessType",
        peripheral_i2c_addr: int,
        node: int,
        data: "List[I2COverDistanceRequest.Data]",
    ) -> I2COverDistanceResponse:
        """Send i2c message to a node and its peripherals.

        :param access_type: read/write/unspecified
        :param peripheral_i2c_addr: number
        :param node: number
        :param data: registry and value to set
        :return: access type and reg values

        """
        i2c_over_distance_request = I2COverDistanceRequest(
            access_type=access_type,
            peripheral_i2c_addr=peripheral_i2c_addr,
            node=node,
            data=data,
        )
        request_packet = RequestPacket(
            i2c_over_distance_request=i2c_over_distance_request
        )
        response = self.client.request(request_packet)
        return response

    def a2b_mailbox_transfer(
        self,
        mailbox_id: int,
        access_type: A2BMailboxAccessType,
        node: int,
        _bytes: int,
        data: RepeatedScalarFieldContainer[int],
    ) -> A2BMailboxTransferResponse:
        """Send/read mailbox data to/from A2B transceiver.

        :param mailbox_id: from json configuration file
        :param access_type: read/write/unspecified
        :param node: id from json configuration file (Slave Node)
        :param _bytes: number of bytes in data
        :param data: to send
        :return: refer to A2BMailboxTransferResponse

        """
        a2b_mailbox_transfer_request = A2BMailboxTransferRequest(
            mailbox_id=mailbox_id,
            access_type=access_type,
            node=node,
            bytes=_bytes,
            data=data,
        )
        request_packet = RequestPacket(
            a2b_mailbox_transfer_request=a2b_mailbox_transfer_request
        )
        response = self.client.request(request_packet)
        return response
