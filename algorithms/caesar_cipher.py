def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Caesar Cipher with multiple shifts (mod 94 printable ASCII).
    """
    result = []
    key_length = len(shift_keys)

    for i, char in enumerate(text):
        shift = shift_keys[i % key_length]
        if ifdecrypt:
            shift = -shift
        new_chr = chr(((ord(char) - 32 + shift) % 94) + 32)
        result.append(new_chr)

    return ''.join(result)
