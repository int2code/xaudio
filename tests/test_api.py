"""Test XAudio"""

from contextlib import contextmanager
from unittest.mock import ANY, patch

import pytest
from device_communication.serial.servers import ThreadedSerialServer

from xaudio.api import XAudioApi
from xaudio.clients import XAudioClient
from xaudio.packetizer import XAudioFramesParser
from xaudio.protocol.interface_pb2 import (  # pylint:disable=no-name-in-module
    A2BDiscoverRequest,
    A2BFaultLocation,
    ConfigJsonState,
    DeviceState,
    I2COverDistanceAccessType,
    I2COverDistanceRequest,
    I2COverDistanceResponse,
    InfoRequest,
    InfoResponse,
    NoDataResponse,
    PositiveResponse,
    RequestPacket,
    ResetRequest,
    ResponsePacket,
    SlaveA2BState,
    StatusRequest,
    StatusResponse,
    StatusRespRoleA2BMaster,
    StatusRespRoleA2BSlave,
    UsbAudioStreamState,
)


class TestXAudioApi:
    """Verify XAudio API responses"""

    @contextmanager
    def patch_serial_on_write_read(self, raw_response):
        """Patch write method of server to trigger reading data."""

        # pylint:disable=unused-argument
        def _trigger_read_on_write(self, data):  # noqa protocol.write API
            self.protocol.data_received(raw_response)

        with patch.object(ThreadedSerialServer, "write", autospec=True) as mock:
            mock.side_effect = _trigger_read_on_write
            yield mock

    @pytest.fixture
    def xaudio_api(self) -> XAudioApi:
        """XAudioApi instance"""
        client = XAudioClient()
        return XAudioApi(client)

    def test_info(self, xaudio_api):
        """Verify info request sending and unpacking."""
        expected_request = (
            ANY,
            XAudioFramesParser.frame(
                RequestPacket(info_request=InfoRequest(dummy=True)).SerializeToString()
            ),
        )
        expected_response = InfoResponse(
            hardware_revision=1, software_revision="2", serial_number="3"
        )
        raw_response = XAudioFramesParser.frame(
            ResponsePacket(
                positive_response=PositiveResponse(info_response=expected_response)
            ).SerializeToString()
        )
        with self.patch_serial_on_write_read(raw_response) as mock_rw:
            response = xaudio_api.info()

        assert response == expected_response
        mock_rw.assert_called_once_with(*expected_request)

    def test_reset(self, xaudio_api):
        """Verify reset request sending and unpacking."""
        expected_request = (
            ANY,
            XAudioFramesParser.frame(
                RequestPacket(
                    reset_request=ResetRequest(dummy=True)
                ).SerializeToString()
            ),
        )
        expected_response = NoDataResponse(dummy=True)
        raw_response = XAudioFramesParser.frame(
            ResponsePacket(
                positive_response=PositiveResponse(no_data_response=expected_response)
            ).SerializeToString()
        )
        with self.patch_serial_on_write_read(raw_response) as mock_rw:
            response = xaudio_api.reset()

        assert response == expected_response
        mock_rw.assert_called_once_with(*expected_request)

    def test_status(self, xaudio_api):
        """Verify reset request sending and unpacking."""
        expected_request = (
            ANY,
            XAudioFramesParser.frame(
                RequestPacket(
                    status_request=StatusRequest(dummy=True)
                ).SerializeToString()
            ),
        )
        expected_response = StatusResponse(
            usb_audio_downstream_state=UsbAudioStreamState.USB_AUDIO_STREAM_STATE_IDLE,
            usb_audio_upstream_state=UsbAudioStreamState.USB_AUDIO_STREAM_STATE_UNSPECIFIED,
            device_state=DeviceState.DEVICE_STATE_NORMAL,
            config_json_state=ConfigJsonState.CONFIG_JSON_STATE_VALID,
            status_master=StatusRespRoleA2BMaster(
                a2b_slaves_discovered=1,
                a2b_fault=StatusRespRoleA2BMaster.A2bFault(
                    fault=1,
                    location=A2BFaultLocation.A2B_FAULT_LOCATION_UNSPECIFIED,
                    slave_with_fault=2,
                ),
            ),
            status_slave=StatusRespRoleA2BSlave(
                a2b_state=SlaveA2BState.SLAVE_A2B_STATE_UNSPECIFIED
            ),
        )
        raw_response = XAudioFramesParser.frame(
            ResponsePacket(
                positive_response=PositiveResponse(status_response=expected_response)
            ).SerializeToString()
        )
        with self.patch_serial_on_write_read(raw_response) as mock_rw:
            response = xaudio_api.status()

        assert response == expected_response
        mock_rw.assert_called_once_with(*expected_request)

    def test_a2b_discover(self, xaudio_api):
        """Verify reset request sending and unpacking."""
        expected_request = (
            ANY,
            XAudioFramesParser.frame(
                RequestPacket(
                    a2b_discover_request=A2BDiscoverRequest(dummy=True)
                ).SerializeToString()
            ),
        )
        expected_response = NoDataResponse(dummy=True)
        raw_response = XAudioFramesParser.frame(
            ResponsePacket(
                positive_response=PositiveResponse(no_data_response=expected_response)
            ).SerializeToString()
        )
        with self.patch_serial_on_write_read(raw_response) as mock_rw:
            response = xaudio_api.a2b_discover()

        assert response == expected_response
        mock_rw.assert_called_once_with(*expected_request)

    def test_i2c_over_distance(self, xaudio_api):
        """Verify i2c_over_distance request sending and unpacking."""
        expected_request = (
            ANY,
            XAudioFramesParser.frame(
                RequestPacket(
                    i2c_over_distance_request=I2COverDistanceRequest(
                        access_type=I2COverDistanceAccessType.I2C_OVER_DISTANCE_READ,
                        peripheral_i2c_addr=1,
                        node=2,
                        data=[I2COverDistanceRequest.Data(reg=8, value=9)],
                    )
                ).SerializeToString()
            ),
        )
        expected_response = I2COverDistanceResponse(value=[9])
        raw_response = XAudioFramesParser.frame(
            ResponsePacket(
                positive_response=PositiveResponse(
                    i2c_over_distance_response=expected_response
                )
            ).SerializeToString()
        )
        with self.patch_serial_on_write_read(raw_response) as mock_rw:
            response = xaudio_api.i2c_over_distance(
                access_type=I2COverDistanceAccessType.I2C_OVER_DISTANCE_READ,
                peripheral_i2c_addr=1,
                node=2,
                data=[I2COverDistanceRequest.Data(reg=8, value=9)],
            )

        assert response == expected_response
        mock_rw.assert_called_once_with(*expected_request)
