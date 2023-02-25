
""" Symmetric Cryptography Problem 

In this problem you will use modes of AES Symmetric algorithm to encrypt and decrypt the messages. AES supportes 
different modes of operation: ECB, CBC, CTR.

Problems:
1. We will use AES-CBC mode to perform encryption and decryption of the input data.
2. We will use AES-CTR mode to perform encryption and decryption of the input data.

ECB mode of operation example is here: https://github.com/kpsubedi/Security/blob/master/cryptography/pythonexample/symmetric_demo.py

To solve these problmes, you need to go through the api documentation here: https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.Cipher
"""

### Problem 1: Use AES CBC Mode to encrypt and decrypt `mytext` ###


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

# Initialize key and initialization vector using urandom() form os package.
import os

key = os.urandom(32)
iv = os.urandom(16)

# This is the message you need to encryt and decrypt 
mytext = b"Welcome to Cloud Security 2023 Spring"

# Complete the following code to complete the CBC mode of operation in AES
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(mytext) + encryptor.finalize()
decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()


### Problem 2: Use AES CTR Mode to decrypt the given cipher test with provided key and iv. ###


# Instantiate a crypto object first for encryption
encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
encrypted = encrypto.encrypt("asdk")

# Instantiate a new crypto object for decryption
decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
print decrypto.decrypt(encrypted)


