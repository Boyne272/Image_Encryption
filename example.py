import numpy as np
from PIL import Image

from Image_Encryption import (str2bin, bin2str,
                              encode_img, decode_image,
                              encrypt_msg, decrypt_msg)


if __name__ == '__main__':

    msg_in = b'enjoy your holiday Anastasia :)'
    print(f'\n\nOriginal msg: {msg_in}')

    # load the image as array
    img = Image.open('imgs/cat.png')
    arr = np.array(img)

    # encrypt the message
    encpt_msg_in = encrypt_msg(msg_in, 'e5 roasthouse')
    print(f'\n\nencpted_msg in: {encpt_msg_in}')

    # convert to binary
    binary_msg_in = str2bin(encpt_msg_in)
    print(f'\n\nBinary msg in: {binary_msg_in}')

    # encode into image
    encoded_img = encode_img(arr, binary_msg_in)
    encoded_pil = Image.fromarray(encoded_img)
    # encoded_pil.save('imgs/cat_encoded.png')

    # decode back out of image
    binary_msg_out = decode_image(encoded_img)
    print(f'\n\nBinary msg out: {binary_msg_out}')
    assert binary_msg_out == binary_msg_in

    # convert binary to string
    encpt_msg_out = bin2str(binary_msg_out)
    print(f'\n\nencrtpyed msg out: {encpt_msg_out}')
    assert encpt_msg_out == encpt_msg_in

    # decrypt the message
    msg_out = decrypt_msg(encpt_msg_out, 'e5 roasthouse')
    print(f'\n\recovered msg: {msg_out}')
    assert msg_out == msg_in
