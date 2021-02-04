# Image_Encryption

Take a message and hide it in an image so that one can not tell the message is there.

## Quick start

run `pip install .` to install.
use the `image_encryption` class which is an API to the underlying utilities to encode and decode images. See example `example_front.py` for an example. If you prefer to see the underlying works see `example_full.py` which leverages pure functional underlying approach.

## Theory

Conert any RGB image into a binary array buy summing the colours and taking even as 0 and odd as 1.Thus any image can be a binary message of length. This process can be reversed, by taking a messageone can perturb each image pixel by 1 in any of the 3 colour channels to create the desired binary message in the image. Adding encryption to this message makes it secret.

## Notes

If this is ever used in any serious context (not that I think it will be) then one should use a real image not a cartoon or computer generated image. This is because the latter tend to have large regions of constance colour, which when perturbed become somewhat objevous (not to the human eye, but to a computer program it is clear). Though the message will still be encrypted I think the fun of this encoder is that any image may or may not have a hidden message and only those who put it there would know for sure.

## Credits

This was written by Richard Boyne one morning in a coffee shop so bare in mind it's simplicity. I have boshed an MIT licence on it so do what you will with it (personally I think it would make for a very good learning excersise for 1st year computing students).

