"""Definition of XAudioAPI - requests that user can make to the device."""

from typing import List, Optional, Tuple

from xaudio.clients import XAudioClient
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    A2BDiscoverRequest,
    A2BMailboxAccessType,
    A2BMailboxTransferRequest,
    A2BMailboxTransferResponse,
    I2COverDistanceAccessType,
    I2COverDistanceRequest,
    I2COverDistanceResponse,
    InfoRequest,
    InfoResponse,
    NoDataResponse,
    RegisterDumpRequest,
    RegisterDumpResponse,
    RequestPacket,
    ResetRequest,
    StatusRequest,
    StatusResponse,
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

    @staticmethod
    def _parse_i2c_data_to_send(
        data: List[Tuple[int, Optional[int]]],
    ) -> List[I2COverDistanceRequest.Data]:
        """Parse pairs of registries and values into I2COverDistanceRequest.Data structure."""
        parsed_data = []
        for reg, val in [(t[0], t[1]) if len(t) == 2 else (t[0], None) for t in data]:
            parsed_data.append(I2COverDistanceRequest.Data(reg=reg, value=val))
        return parsed_data

    def i2c_over_distance(
        self,
        node: int,
        access_type: "I2COverDistanceAccessType",
        data: List[Tuple[int, Optional[int]]],  #  "List[I2COverDistanceRequest.Data]",
        peripheral_i2c_addr: Optional[int] = None,
    ) -> I2COverDistanceResponse:
        """Send I2C message to a node or its peripherals.

        Used to read/write data from/to node (or its peripherals) registries over I2C.
        Look at the example below to read data from slave node registries:

            >>> client = XAudioClient("COM5")
            >>> to_send = [(0x01, 0x02), (0x02, None), (0x03,)]
            >>> read = I2COverDistanceAccessType.I2C_OVER_DISTANCE_READ  # or write
            >>> api = XAudioApi(client)
            >>> resp = api.i2c_over_distance(
            ...     node=0,
            ...     access_type=read,
            ...     data=to_send
            ...   # peripheral_i2c_addr=None,  # address of the peripheral device if used
            ... )
            >>> print(resp)

        And to write the data back to slave node registries:

            >>> client = XAudioClient("COM5")
            >>> to_send = [(0x01, 0xFF), (0x02, 0x00), (0x03, 0xAB)]
            >>> read = I2COverDistanceAccessType.I2C_OVER_DISTANCE_READ  # or write
            >>> api = XAudioApi(client)
            >>> resp = api.i2c_over_distance(
            ...     node=0,
            ...     access_type=read,
            ...     data=to_send
            ...   # peripheral_i2c_addr=None,  # address of the peripheral device if used
            ... )
            >>> print(resp)

        :param node: number, specified in the json configuration
        :param access_type: read/write/unspecified
        :param data: list of pairs (registry, value) to read/write,
            value is ignored on read
        :param peripheral_i2c_addr: if not given the operation will be performed
            directly on node and not its peripherals
        :return: access type and reg values

        """
        data = self._parse_i2c_data_to_send(data)
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
        node: int,
        mailbox_id: int,
        access_type: A2BMailboxAccessType,
        _bytes: Optional[int] = None,
        data: Optional[list[int]] = None,
    ) -> A2BMailboxTransferResponse:
        """Send/read mailbox data to/from A2B transceiver.

        Sample use:

            >>> client = XAudioClient("COM5")
            >>> to_send = [0x00, 0x01, 0x02, 0x03]  # 4 bytes
            >>> write = A2BMailboxAccessType.A2B_MAILBOX_ACCESS_TYPE_WRITE
            >>> api = XAudioApi(client)
            >>> resp = api.a2b_mailbox_transfer(
            ...     node=0,
            ...     access_type=write,
            ...     data=to_send,
            ...   # _bytes=4,  # len(data) required on read, auto calculated on write
            ... )
            >>> print(resp)

        :param node: id from json configuration file (Slave)
        :param mailbox_id: slave mailbox id from config file
        :param access_type: read/write/unspecified
        :param _bytes: number of bytes to read or write, on write it's len(data)
        :param data: list of bytes to send
        :return: refer to A2BMailboxTransferResponse fields

        """
        if data is None:
            data = []
        a2b_mailbox_transfer_request = A2BMailboxTransferRequest(
            mailbox_id=mailbox_id,
            access_type=access_type,
            node=node,
            bytes=_bytes or len(data),
            data=data,
        )
        request_packet = RequestPacket(
            a2b_mailbox_transfer_request=a2b_mailbox_transfer_request
        )
        response = self.client.request(request_packet)
        return response

    def register_dump(self, node: int | None) -> RegisterDumpResponse:
        """Dump register values of A2B transceiver.

        :param node: id from json configuration file (Slave).
        If None, dumps registries from A2Bridge
        :return: refer to RegisterDumpResponse fields

        """
        register_dump_request = RegisterDumpRequest(node_number=node)
        request_packet = RequestPacket(register_dump_request=register_dump_request)
        response = self.client.request(request_packet)
        return response
