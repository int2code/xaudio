"""Communication handlers for XAudio"""

from device_communication.serial.communication_handlers import (
    SerialCommunicationHandler,
)

from xaudio.packetizer import XAudioPacketizer


class XAudioSerialCommHandler(SerialCommunicationHandler):
    """Serial communication handler with XAudio protocol class."""

    SERIAL_PROTOCOL_CLS = XAudioPacketizer
