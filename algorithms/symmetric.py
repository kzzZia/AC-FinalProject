from Cryptodome.Cipher import AES, DES
from cryptography.fernet import Fernet
import base64, os

# AES (with ECB mode for simplicity)
def pad(text): return text + (16 - len(text) % 16) * chr(16 - len(text) % 16)
def unpad(text): return text[:-ord(text[-1])]

def aes_encrypt(text):
    key = b"ThisIsASecretKey"
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text)
    return base64.b64encode(cipher.encrypt(padded_text.encode())).decode()

def aes_decrypt(enc):
    key = b"ThisIsASecretKey"
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc)).decode())

# DES
def des_encrypt(text):
    key = b"8bytekey"
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad(text)
    return base64.b64encode(cipher.encrypt(padded.encode())).decode()

def des_decrypt(enc):
    key = b"8bytekey"
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc)).decode())

# Fernet (AES + HMAC)
fernet_key = Fernet.generate_key()
fernet_cipher = Fernet(fernet_key)

def fernet_encrypt(text): return fernet_cipher.encrypt(text.encode()).decode()
def fernet_decrypt(enc): return fernet_cipher.decrypt(enc.encode()).decode()
