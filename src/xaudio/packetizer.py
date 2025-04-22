"""Module provides classes to read/write binary data."""

import logging
from typing import List, Tuple

from cobs import cobs
from device_communication.base.packetizer import BaseFrameParser
from device_communication.serial.servers import ThreadedSerialServer
from libscrc import mpeg2  # pylint:disable=no-name-in-module
from serial.threaded import Packetizer

logger = logging.getLogger(__name__)


class XAudioFramesParser(BaseFrameParser):
    """XAudio frame parser."""

    TERMINATOR = b"\x00"
    CRC_SIZE = 4

    @classmethod
    def frame(cls, data: bytearray) -> bytearray:
        """Frame data buffer

        Calculate 4B CRC32/MPEG2 and encode whole buffer with COBS - end with terminator.

        :param data: buffer to send
        :return: encoded data with CRC and terminator

        """
        return cobs.encode(data + mpeg2(data).to_bytes(cls.CRC_SIZE)) + cls.TERMINATOR

    @classmethod
    def parse_frames(
        cls, buffer: bytearray
    ) -> Tuple[List[bytearray], bytearray, bytearray]:
        """Parse given buffer to frames

        :param buffer: incoming data stream
        :returns:
            parsed XAudio frames found in buffer,
            remaining buffer,
            dropped data (CRC did not match)

        """
        packets = []
        dropped = bytearray()
        while cls.TERMINATOR in buffer:
            packet, buffer = buffer.split(cls.TERMINATOR, 1)
            packet = cobs.decode(packet)
            packet, crc = packet[: -cls.CRC_SIZE], packet[-cls.CRC_SIZE :]
            if not crc == mpeg2(packet).to_bytes(cls.CRC_SIZE):
                dropped.extend(packet + crc)
            else:
                packets.append(packet)
        return packets, buffer, dropped


class XAudioPacketizer(Packetizer):
    """Read/write data from/to serial port.

    The COBS encoding with CRC32/MPEG2 (4B) and terminator are applied.

    """

    FRAME_PARSER_CLS = XAudioFramesParser

    def __init__(self):
        super().__init__()
        self.transport: ThreadedSerialServer = None  # noqa

    def connection_made(self, transport):
        """Store transport"""
        self.transport = transport

    def connection_lost(self, exc):
        """Forget transport"""
        self.transport = None
        super(Packetizer, self).connection_lost(exc)

    def data_received(self, data):
        """Buffer received data, find TERMINATOR, call handle_packet"""
        self.buffer.extend(data)
        packets, self.buffer, dropped = self.FRAME_PARSER_CLS.parse_frames(self.buffer)

        for packet in packets:
            self.handle_packet(packet)

        self.handle_dropped_packet(dropped)

    def handle_packet(self, packet: bytearray):
        """Process packet - store in queue for client to read"""
        self.transport.incoming_buffer.put_nowait(packet)

    def handle_dropped_packet(self, packet: bytearray):
        """Process dropped packets - store in queue"""
        logger.debug("Could not parse data: %s", packet.hex(" "))

    def send(self, data: bytearray):
        """Prepare packet and send it to transport for write"""
        self.transport.write(self.FRAME_PARSER_CLS.frame(data))
