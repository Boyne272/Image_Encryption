"""Fucntions for encrypting your binary message.

Made using the following reference materials:
- https://www.youtube.com/watch?time_continue=82&v=H8t4DJ3Tdrg&feature=emb_logo
- https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
"""

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def pass_to_key(password):
    """Return a key from the given password for encryption."""
    byte_pass = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"\r7\xb6bT\xa0\xd5\xdcG.'+\xb7\xdb\r\xcd",
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(byte_pass))


def encrypt_msg(msg, password):
    assert isinstance(msg, bytes)
    f = Fernet(pass_to_key(password))
    return f.encrypt(msg)


def decrypt_msg(msg, password):
    assert isinstance(msg, bytes)
    f = Fernet(pass_to_key(password))
    return f.decrypt(msg)


if __name__ == '__main__':
    msg = b'I am a tea pot'
    print(f'\n\nOriginal msg: {msg, type(msg)}')
    encrypted_msg = encrypt_msg(msg, 'test_password')
    print(f'\n\nEncrypted msg: {encrypted_msg, type(encrypted_msg)}')
    decrypted_msg = decrypt_msg(encrypted_msg, 'test_password')
    print(f'\n\nDecrypted msg: {decrypted_msg, type(decrypted_msg)}')
