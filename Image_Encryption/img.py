import random


def encode_img(img_array, binary):
    """
    Loops through the image pixles and purturbes values slightly so that
    a pixles.sum % 2 is the given binary message
    also makes the first 16 bits hold meta data for the message length
    """
    bin_length = bin(int(len(binary)))[2:].zfill(16)
    binary = bin_length + binary.decode()
    for pixel, bin_val in zip(img_array.reshape(-1, 3), binary):
        if pixel.sum() % 2 != int(bin_val):
            i = random.randint(0, 2)
            delta = (-1 if pixel[i] == 255
                     else +1 if pixel[i] == 0
                     else random.choice([1, -1]))
            pixel[i] += delta
            assert pixel.sum() % 2 == int(bin_val)
    return img_array


def decode_image(img_array):
    'converts the given image into binary'
    bin_arr = img_array.reshape(-1, 3).sum(axis=1) % 2
    bin_str = ''.join([str(c) for c in bin_arr])
    msg_len = int(bin_str[:16], 2)
    return bin_str[16: msg_len+16].encode()
