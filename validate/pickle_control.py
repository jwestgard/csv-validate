#!/usr/bin/python3

import pickle

control = [ (b'\x00', 'NUL', '␀', '^@', 'Null Character'),
(b'\x01', 'SOH', '␁', '^A', 'Start of Header'),
(b'\x02', 'STX', '␂', '^B', 'Start of Text'),
(b'\x03', 'ETX', '␃', '^C', 'End of Text'),
(b'\x04', 'EOT', '␄', '^D', 'End of Transmission'),
(b'\x05', 'ENQ', '␅', '^E', 'Enquiry'),
(b'\x06', 'ACK', '␆', '^F', 'Acknowledgment'),
(b'\x07', 'BEL', '␇', '^G', 'Bell'),
(b'\x08', 'BS', '␈', '^H', 'Backspace'),
(b'\x09', 'HT', '␉', '^I', 'Horizontal Tab'),
(b'\x0A', 'LF', '␊', '^J', 'Line Feed'),
(b'\x0B', 'VT', '␋', '^K', 'Vertical Tab'),
(b'\x0C', 'FF', '␌', '^L', 'Form Feed'),
(b'\x0D', 'CR', '␍', '^M', 'Carriage Return'),
(b'\x0E', 'SO', '␎', '^N', 'Shift Out'),
(b'\x0F', 'SI', '␏', '^O', 'Shift In'),
(b'\x10', 'DLE', '␐', '^P', 'Data Link Escape'),
(b'\x11', 'DC1', '␑', '^Q', 'Device Control 1 (oft. XON)'),
(b'\x12', 'DC2', '␒', '^R', 'Device Control 2'),
(b'\x13', 'DC3', '␓', '^S', 'Device Control 3 (oft. XOFF)'),
(b'\x14', 'DC4', '␔', '^T', 'Device Control 4'),
(b'\x15', 'NAK', '␕', '^U', 'Negative Acknowledgment'),
(b'\x16', 'SYN', '␖', '^V', 'Synchronous Idle'),
(b'\x17', 'ETB', '␗', '^W', 'End of Transmission Block'),
(b'\x18', 'CAN', '␘', '^X', 'Cancel'),
(b'\x19', 'EM', '␙', '^Y', 'End of Medium'),
(b'\x1A', 'SUB', '␚', '^Z', 'Substitute'),
(b'\x1B', 'ESC', '␛', '^[', 'Escape'),
(b'\x1C', 'FS', '␜', '^\', 'File Separator'),
(b'\x1D', 'GS', '␝', '^]', 'Group Separator'),
(b'\x1E', 'RS', '␞', '^^', 'Record Separator'),
(b'\x1F', 'US', '␟', '^_', 'Unit Separator'),
(b'\x7F', 'DEL', '␡', '^?', 'Delete') ]

for x in control:
	print(x)
