"""Class for handling strings"""


def str2bin(msg):
    """Convert a binary string into a 16 bit binary message."""
    assert isinstance(msg, bytes), 'must give a byte obj'
    return ''.join([bin(c)[2:].zfill(16) for c in msg]).encode()


def bin2str(binary):
    """Convert biary 16 bit binary message into a string of chars."""
    assert isinstance(binary, bytes), 'must give a byte obj'
    assert len(binary) % 16 == 0, 'must have 16 bit valuess'
    return ''.join([chr(int(binary[n: n+16], 2))
                    for n in range(0, len(binary), 16)]).encode()
