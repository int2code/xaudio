"""Test XAudioClients"""

from unittest.mock import DEFAULT, Mock, patch

import pytest

from xaudio.clients import XAudioClient
from xaudio.communication_handlers import XAudioSerialCommHandler
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    RequestPacket,
)


class TestXAudioClient:
    """Verify XAudioClient functionality"""

    def test_too_many_responses_for_request(self):
        """Verify exception is raised if more than one response msg is returned"""
        with patch.multiple(
            XAudioSerialCommHandler, send=DEFAULT, receive=Mock(return_value=[b""] * 2)
        ):
            client = XAudioClient()
            with pytest.raises(RuntimeError, match="Too many responses"):
                client.request(RequestPacket())

    def test_response_packet_is_missing_msg(self):
        """Verify exception raise when response is missing Positive/Negative msg"""
        with patch.multiple(
            XAudioSerialCommHandler, send=DEFAULT, receive=Mock(return_value=[b""])
        ):
            client = XAudioClient()
            with pytest.raises(RuntimeError, match="missing Positive or Negative msg"):
                client.request(RequestPacket())

    def test_negative_response_raise_exception(self):
        """Verify exception is raised when device sends negative response"""
        with patch.multiple(
            XAudioSerialCommHandler,
            send=DEFAULT,
            receive=Mock(return_value=[b"\x12\x02\x08\x01"]),
        ):
            client = XAudioClient()
            with pytest.raises(RuntimeError, match="returned negative response"):
                client.request(RequestPacket())
