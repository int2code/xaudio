### 0.3.0

[MINOR] Added support for A2B Mailboxes

- added API method `a2b_mailbox_transfer` to transfer data to and read from A2B slave 
mailboxes. Modified 
- modified `i2c_over_distance` API to better suite its usage
- improved documentation, added sample use for mentioned methods

### 0.2.0

[MINOR] Improved XAudio API.

Added:
- timeout to wait for response from device
- custom exceptions

Fixed wrongly parsed CRC. Updated protobuf with new version.

### 0.1.0

[MINOR] Initial release.

Initial release with XAudio communication implementation.