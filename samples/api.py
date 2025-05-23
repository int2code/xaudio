"""Quick sample use of XAudio Client and API."""

# pylint:disable=no-name-in-module

from xaudio.api import XAudioApi
from xaudio.clients import XAudioClient
from xaudio.protocol.interface_pb2 import InfoRequest, RequestPacket

# Replace with actual COM port where XAudio is connected
COM_PORT = "COM99"
client = XAudioClient(COM_PORT, f"XAudio_on_{COM_PORT}")

# Send sample request with the generic request
# from XAudio client -> each request must return
# single response msg even when calling reset
sample_msg = RequestPacket(info_request=InfoRequest(dummy=True)).SerializeToString()
response = client.request(sample_msg)
print(response)


# Convenient API client for sending and reading messages
# with simplified message building
api_client = XAudioApi(client)
response = api_client.info()
print(response.serial_number)
print(response.hardware_revision)
print(response.software_revision)

response = api_client.status()
print(response)
