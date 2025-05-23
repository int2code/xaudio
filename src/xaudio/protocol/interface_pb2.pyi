from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

import nanopb_pb2 as _nanopb_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class A2BFaultLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    A2B_FAULT_LOCATION_UNSPECIFIED: _ClassVar[A2BFaultLocation]
    A2B_FAULT_LOCATION_MASTER: _ClassVar[A2BFaultLocation]
    A2B_FAULT_LOCATION_SLAVE: _ClassVar[A2BFaultLocation]

class SlaveA2BState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLAVE_A2B_STATE_UNSPECIFIED: _ClassVar[SlaveA2BState]
    SLAVE_A2B_STATE_INIT: _ClassVar[SlaveA2BState]
    SLAVE_A2B_STATE_WAIT_DISCOVER: _ClassVar[SlaveA2BState]
    SLAVE_A2B_STATE_READY: _ClassVar[SlaveA2BState]
    SLAVE_A2B_STATE_NOT_READY: _ClassVar[SlaveA2BState]

class UsbAudioStreamState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USB_AUDIO_STREAM_STATE_UNSPECIFIED: _ClassVar[UsbAudioStreamState]
    USB_AUDIO_STREAM_STATE_IDLE: _ClassVar[UsbAudioStreamState]
    USB_AUDIO_STREAM_STATE_STREAMING: _ClassVar[UsbAudioStreamState]

class DeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_STATE_UNSPECIFIED: _ClassVar[DeviceState]
    DEVICE_STATE_BOOT: _ClassVar[DeviceState]
    DEVICE_STATE_NORMAL: _ClassVar[DeviceState]
    DEVICE_STATE_IMPAIRED: _ClassVar[DeviceState]
    DEVICE_STATE_ERROR: _ClassVar[DeviceState]

class I2COverDistanceAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    I2C_OVER_DISTANCE_UNSPECIFIED: _ClassVar[I2COverDistanceAccessType]
    I2C_OVER_DISTANCE_WRITE: _ClassVar[I2COverDistanceAccessType]
    I2C_OVER_DISTANCE_READ: _ClassVar[I2COverDistanceAccessType]

class ConfigJsonState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIG_JSON_STATE_UNSPECIFIED: _ClassVar[ConfigJsonState]
    CONFIG_JSON_STATE_VALID: _ClassVar[ConfigJsonState]
    CONFIG_JSON_STATE_INVALID: _ClassVar[ConfigJsonState]

A2B_FAULT_LOCATION_UNSPECIFIED: A2BFaultLocation
A2B_FAULT_LOCATION_MASTER: A2BFaultLocation
A2B_FAULT_LOCATION_SLAVE: A2BFaultLocation
SLAVE_A2B_STATE_UNSPECIFIED: SlaveA2BState
SLAVE_A2B_STATE_INIT: SlaveA2BState
SLAVE_A2B_STATE_WAIT_DISCOVER: SlaveA2BState
SLAVE_A2B_STATE_READY: SlaveA2BState
SLAVE_A2B_STATE_NOT_READY: SlaveA2BState
USB_AUDIO_STREAM_STATE_UNSPECIFIED: UsbAudioStreamState
USB_AUDIO_STREAM_STATE_IDLE: UsbAudioStreamState
USB_AUDIO_STREAM_STATE_STREAMING: UsbAudioStreamState
DEVICE_STATE_UNSPECIFIED: DeviceState
DEVICE_STATE_BOOT: DeviceState
DEVICE_STATE_NORMAL: DeviceState
DEVICE_STATE_IMPAIRED: DeviceState
DEVICE_STATE_ERROR: DeviceState
I2C_OVER_DISTANCE_UNSPECIFIED: I2COverDistanceAccessType
I2C_OVER_DISTANCE_WRITE: I2COverDistanceAccessType
I2C_OVER_DISTANCE_READ: I2COverDistanceAccessType
CONFIG_JSON_STATE_UNSPECIFIED: ConfigJsonState
CONFIG_JSON_STATE_VALID: ConfigJsonState
CONFIG_JSON_STATE_INVALID: ConfigJsonState

class ResetRequest(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class StatusRequest(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class A2BDiscoverRequest(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class InfoRequest(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class SetSerialRequest(_message.Message):
    __slots__ = ("serial_number", "lock")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOCK_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    lock: bool
    def __init__(
        self, serial_number: _Optional[str] = ..., lock: bool = ...
    ) -> None: ...

class I2COverDistanceRequest(_message.Message):
    __slots__ = ("access_type", "peripheral_i2c_addr", "node", "data")

    class Data(_message.Message):
        __slots__ = ("reg", "value")
        REG_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        reg: int
        value: int
        def __init__(
            self, reg: _Optional[int] = ..., value: _Optional[int] = ...
        ) -> None: ...

    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERIPHERAL_I2C_ADDR_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    access_type: I2COverDistanceAccessType
    peripheral_i2c_addr: int
    node: int
    data: _containers.RepeatedCompositeFieldContainer[I2COverDistanceRequest.Data]
    def __init__(
        self,
        access_type: _Optional[_Union[I2COverDistanceAccessType, str]] = ...,
        peripheral_i2c_addr: _Optional[int] = ...,
        node: _Optional[int] = ...,
        data: _Optional[_Iterable[_Union[I2COverDistanceRequest.Data, _Mapping]]] = ...,
    ) -> None: ...

class I2COverDistanceResponse(_message.Message):
    __slots__ = ("access_type", "value")
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    access_type: I2COverDistanceAccessType
    value: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        access_type: _Optional[_Union[I2COverDistanceAccessType, str]] = ...,
        value: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class NoDataResponse(_message.Message):
    __slots__ = ("dummy",)
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    dummy: bool
    def __init__(self, dummy: bool = ...) -> None: ...

class StatusRespRoleA2BMaster(_message.Message):
    __slots__ = ("a2b_slaves_discovered", "a2b_fault")

    class A2bFault(_message.Message):
        __slots__ = ("fault", "location", "slave_with_fault")
        FAULT_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        SLAVE_WITH_FAULT_FIELD_NUMBER: _ClassVar[int]
        fault: int
        location: A2BFaultLocation
        slave_with_fault: int
        def __init__(
            self,
            fault: _Optional[int] = ...,
            location: _Optional[_Union[A2BFaultLocation, str]] = ...,
            slave_with_fault: _Optional[int] = ...,
        ) -> None: ...

    A2B_SLAVES_DISCOVERED_FIELD_NUMBER: _ClassVar[int]
    A2B_FAULT_FIELD_NUMBER: _ClassVar[int]
    a2b_slaves_discovered: int
    a2b_fault: StatusRespRoleA2BMaster.A2bFault
    def __init__(
        self,
        a2b_slaves_discovered: _Optional[int] = ...,
        a2b_fault: _Optional[_Union[StatusRespRoleA2BMaster.A2bFault, _Mapping]] = ...,
    ) -> None: ...

class StatusRespRoleA2BSlave(_message.Message):
    __slots__ = ("a2b_state",)
    A2B_STATE_FIELD_NUMBER: _ClassVar[int]
    a2b_state: SlaveA2BState
    def __init__(
        self, a2b_state: _Optional[_Union[SlaveA2BState, str]] = ...
    ) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = (
        "usb_audio_downstream_state",
        "usb_audio_upstream_state",
        "device_state",
        "config_json_state",
        "status_master",
        "status_slave",
    )
    USB_AUDIO_DOWNSTREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    USB_AUDIO_UPSTREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_JSON_STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MASTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_SLAVE_FIELD_NUMBER: _ClassVar[int]
    usb_audio_downstream_state: UsbAudioStreamState
    usb_audio_upstream_state: UsbAudioStreamState
    device_state: DeviceState
    config_json_state: ConfigJsonState
    status_master: StatusRespRoleA2BMaster
    status_slave: StatusRespRoleA2BSlave
    def __init__(
        self,
        usb_audio_downstream_state: _Optional[_Union[UsbAudioStreamState, str]] = ...,
        usb_audio_upstream_state: _Optional[_Union[UsbAudioStreamState, str]] = ...,
        device_state: _Optional[_Union[DeviceState, str]] = ...,
        config_json_state: _Optional[_Union[ConfigJsonState, str]] = ...,
        status_master: _Optional[_Union[StatusRespRoleA2BMaster, _Mapping]] = ...,
        status_slave: _Optional[_Union[StatusRespRoleA2BSlave, _Mapping]] = ...,
    ) -> None: ...

class InfoResponse(_message.Message):
    __slots__ = ("hardware_revision", "software_revision", "serial_number")
    HARDWARE_REVISION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_REVISION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    hardware_revision: int
    software_revision: str
    serial_number: str
    def __init__(
        self,
        hardware_revision: _Optional[int] = ...,
        software_revision: _Optional[str] = ...,
        serial_number: _Optional[str] = ...,
    ) -> None: ...

class PositiveResponse(_message.Message):
    __slots__ = (
        "no_data_response",
        "status_response",
        "info_response",
        "i2c_over_distance_response",
    )
    NO_DATA_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    I2C_OVER_DISTANCE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    no_data_response: NoDataResponse
    status_response: StatusResponse
    info_response: InfoResponse
    i2c_over_distance_response: I2COverDistanceResponse
    def __init__(
        self,
        no_data_response: _Optional[_Union[NoDataResponse, _Mapping]] = ...,
        status_response: _Optional[_Union[StatusResponse, _Mapping]] = ...,
        info_response: _Optional[_Union[InfoResponse, _Mapping]] = ...,
        i2c_over_distance_response: _Optional[
            _Union[I2COverDistanceResponse, _Mapping]
        ] = ...,
    ) -> None: ...

class NegativeResponse(_message.Message):
    __slots__ = ("no_data", "text_error")
    NO_DATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_ERROR_FIELD_NUMBER: _ClassVar[int]
    no_data: bool
    text_error: str
    def __init__(
        self, no_data: bool = ..., text_error: _Optional[str] = ...
    ) -> None: ...

class RequestPacket(_message.Message):
    __slots__ = (
        "reset_request",
        "a2b_discover_request",
        "status_request",
        "info_request",
        "set_serial_request",
        "i2c_over_distance_request",
    )
    RESET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    A2B_DISCOVER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STATUS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_SERIAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    I2C_OVER_DISTANCE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    reset_request: ResetRequest
    a2b_discover_request: A2BDiscoverRequest
    status_request: StatusRequest
    info_request: InfoRequest
    set_serial_request: SetSerialRequest
    i2c_over_distance_request: I2COverDistanceRequest
    def __init__(
        self,
        reset_request: _Optional[_Union[ResetRequest, _Mapping]] = ...,
        a2b_discover_request: _Optional[_Union[A2BDiscoverRequest, _Mapping]] = ...,
        status_request: _Optional[_Union[StatusRequest, _Mapping]] = ...,
        info_request: _Optional[_Union[InfoRequest, _Mapping]] = ...,
        set_serial_request: _Optional[_Union[SetSerialRequest, _Mapping]] = ...,
        i2c_over_distance_request: _Optional[
            _Union[I2COverDistanceRequest, _Mapping]
        ] = ...,
    ) -> None: ...

class ResponsePacket(_message.Message):
    __slots__ = ("positive_response", "negative_response")
    POSITIVE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    positive_response: PositiveResponse
    negative_response: NegativeResponse
    def __init__(
        self,
        positive_response: _Optional[_Union[PositiveResponse, _Mapping]] = ...,
        negative_response: _Optional[_Union[NegativeResponse, _Mapping]] = ...,
    ) -> None: ...
