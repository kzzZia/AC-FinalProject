import rsa

(pubkey, privkey) = rsa.newkeys(512)

def rsa_encrypt(text):
    return rsa.encrypt(text.encode(), pubkey).hex()

def rsa_decrypt(enc_hex):
    enc_bytes = bytes.fromhex(enc_hex)
    return rsa.decrypt(enc_bytes, privkey).decode()

# ECC mock (actual ECC needs third-party or OpenSSL handling)
def ecc_encrypt(text): return f"ECC_ENCRYPTED({text})"
def ecc_decrypt(text): return text.replace("ECC_ENCRYPTED(", "").replace(")", "")
