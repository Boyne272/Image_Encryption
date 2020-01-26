from Image_Encryption import image_encryption


if __name__ == '__main__':

    # input
    msg_in = b'enjoy your holiday Anastasia :)'
    img_in = 'imgs/cat.png'
    img_out = 'imgs/cat_encoded.png'
    print(f'\nInput msg: {msg_in}')

    obj = image_encryption(msg_in, img_in)
    obj.encrypt('test_password')
    print(f'\nEncrypted msg: {obj.msg}')
    obj.encode()
    obj.save_image(img_out, overwirte=True)

    obj2 = image_encryption(img_path=img_out)
    obj2.decode()
    obj2.decrypt(password='test_password')
    print(f'\nRecovered msg: {obj2.msg}')

    assert obj2.msg == msg_in
