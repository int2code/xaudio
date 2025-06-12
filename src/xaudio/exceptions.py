"""XAudio defined exceptions and errors."""


class XAudioException(Exception):
    """Base class for other XAudio exceptions."""


class XAudioTimeoutError(XAudioException):
    """Raised when XAudio did not respond in expected time."""


class XAudioResponseError(XAudioException):
    """Unexpected response detected."""
