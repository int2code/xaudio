"""Test XAudioClients"""

from unittest.mock import DEFAULT, Mock, patch

import pytest

from xaudio.clients import XAudioClient
from xaudio.communication_handlers import XAudioSerialCommHandler
from xaudio.exceptions import XAudioResponseError
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    NoDataResponse,
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
            with pytest.raises(XAudioResponseError, match="Too many responses"):
                client.request(RequestPacket())

    def test_response_no_data_packet(self):
        """Verify no data packet is returned on empty bytes."""
        with patch.multiple(
            XAudioSerialCommHandler, send=DEFAULT, receive=Mock(return_value=[b""])
        ):
            client = XAudioClient()
            response = client.request(RequestPacket())
            assert isinstance(response, NoDataResponse)

    def test_negative_response_raise_exception(self):
        """Verify exception is raised when device sends negative response"""
        with patch.multiple(
            XAudioSerialCommHandler,
            send=DEFAULT,
            receive=Mock(return_value=[b"\x12\x02\x08\x01"]),
        ):
            client = XAudioClient()
            with pytest.raises(XAudioResponseError, match="returned negative response"):
                client.request(RequestPacket())
