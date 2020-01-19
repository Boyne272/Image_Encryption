# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:30:45 2020

@author: Boyne
"""

import sys
import random
import numpy as np
from PIL import Image


def str2bin(msg):
    '''
    convert a string into a 16 bit binary message
    '''
    assert isinstance(msg, str), 'must give a string'
    return ''.join([bin(ord(c))[2:].zfill(16) for c in msg])


def bin2str(binary):
    '''
    convert biary 16 bit binary message into a string of chars
    '''
    assert len(binary) % 16 == 0, 'must have 16 bit valuess'
    return ''.join([chr(int(binary[n:n+16], 2)) for n in range(0, len(binary), 16)])


def encode_img(img_array, binary):
    '''
    loops through the image pixles and purturbes values slightly so that
    a pixles.sum % 2 is the given binary message
    also makes the first 16 bits hold meta data for the message length
    '''
    binary = bin(int(len(binary)))[2:].zfill(16) + binary
    for pixel, bin_val in zip(img_array.reshape(-1, 3), binary):
        if pixel.sum() % 2 != int(bin_val):
            i = random.randint(0, 2)
            delta = -1 if pixel[i] == 255 else\
                    +1 if pixel[i] == 0 else\
                    random.choice([+1,-1])
            pixel[i] += delta
            assert pixel.sum() % 2 == int(bin_val)
    return img_array


def decode_image(img_array):
    'converts the given image into binary'
    bin_arr = img_array.reshape(-1, 3).sum(axis=1) % 2
    bin_str = ''.join([str(c) for c in bin_arr])
    msg_len = int(bin_str[:16], 2)
    return bin_str[16:msg_len+16]

# if __name__ == '__main__':
#     msg = 'Enjoy your holiday Anastasia :)'
#     binary_msg = str2bin(msg)
#     print(bin2str(binary_msg))

if __name__ == '__main__':
    
    msg = 'enjoy your holiday Anastasia :)'
    print('original msg:', msg)

    # load the image as array
    img = Image.open(r'\Users\Boyne\Desktop\image_encription\imgs\cat.png')
    arr = np.array(img)
    # img.show()

    # convert msg to binary
    binary_msg = str2bin(msg)
    print('bin msg in:', binary_msg[16:], '\n')

    # encode into image
    encoded_img = encode_img(arr, binary_msg)
    encoded_pil = Image.fromarray(encoded_img)
    encoded_pil.show()

    # decode back out of image
    decoded_binary = decode_image(encoded_img)
    print('bin msg out:', decoded_binary)
    print('recovered message:', bin2str(decoded_binary))
