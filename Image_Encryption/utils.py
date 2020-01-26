"""Holds vairous Miscellanious functions."""


import os
import numpy as np
from PIL import Image
from .encrypt import encrypt_msg, decrypt_msg
from .img import encode_img, decode_img
from .msg import bin2str, str2bin


class Img_Base():
    """Parent Class for basic image manipulation."""
    def __init__(self):
        self.arr = None

    def load_image(self, path):
        """Load the given image"""
        if not path:
            return None
        elif not os.path.isfile(path):
            raise ValueError(f'file at {path} not found')

        self.arr = np.array(Image.open(path))

    def save_image(self, path, overwirte=False):
        """Save the current image."""
        if self.arr is None:
            raise AttributeError('No image currently loaded')
        elif os.path.isfile(path) and not overwirte:
            raise ValueError(f'file at {path} already exists')

        Image.fromarray(self.arr).save(path)

    def show_image(self):
        """Display the current image."""
        if self.arr is None:
            raise AttributeError('no image loaded yet')

        Image.fromarray(self.arr).show()


class image_encryption(Img_Base):
    """A front end class for image encryption."""

    def __init__(self, msg=None, img_path=None):
        """Initalise with as much or as little data as wanted"""
        super(Img_Base, self).__init__()
        self.msg = None

        # call assignment functions
        self.set_msg(msg)
        self.load_image(img_path)

    def set_msg(self, msg):
        """Set the given msg"""
        if msg is None:
            return None
        if isinstance(msg, str):
            self.msg = msg.encode()
        elif isinstance(msg, bytes):
            self.msg = msg
        else:
            raise TypeError('msg must be either a str or bytes obj')

    def encrypt(self, password):
        """Encrypt the current msg with a password."""
        if not self.msg:
            raise AttributeError('msg not given yet')
        if not isinstance(password, str):
            raise TypeError('password must be a string')

        self.msg = encrypt_msg(self.msg, password)

    def decrypt(self, password):
        """Encrypt the current msg with a password."""
        if not self.msg:
            raise AttributeError('msg not given yet')
        if not isinstance(password, str):
            raise TypeError('password must be a string')

        self.msg = decrypt_msg(self.msg, password)

    def encode(self):
        """Encode the given msg onto the given image."""
        if not self.msg:
            raise AttributeError('message not given yet')
        elif self.arr is None:
            raise AttributeError('image not given yet')

        self.arr = encode_img(self.arr, str2bin(self.msg))

    def decode(self):
        """Decode the msg out of the given img."""
        if self.arr is None:
            raise AttributeError('image not given yet')

        self.msg = bin2str(decode_img(self.arr))
