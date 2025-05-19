def xor_cipher(text, key):
    result = []
    log = []

    for i in range(len(text)):
        p_char = text[i]
        k_char = key[i % len(key)]
        xor_value = ord(p_char) ^ ord(k_char)

        log.append({
            "index": i,
            "p_char": p_char,
            "p_bin": format(ord(p_char), '08b'),
            "k_char": k_char,
            "k_bin": format(ord(k_char), '08b'),
            "xor_bin": format(xor_value, '08b'),
            "xor_char": chr(xor_value) if 32 <= xor_value <= 126 else repr(chr(xor_value))
        })

        result.append(chr(xor_value))

    return ''.join(result), log
