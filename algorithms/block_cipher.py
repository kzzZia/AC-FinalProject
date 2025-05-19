def padding_message(message, block_size=8, padding_char='_'):
    padding_length = (block_size - len(message) % block_size) % block_size
    return message + (padding_char * padding_length)

def remove_padding(message, padding_char='_'):
    return message.rstrip(padding_char)

def xor_operation(block, key):
    return [ord(b) ^ ord(k) for b, k in zip(block, key)]

def encrypt(text, key):
    text = padding_message(text)
    result = []

    for i in range(0, len(text), 8):
        block = text[i:i+8]
        encrypted_block = xor_operation(block, key)
        result.extend(encrypted_block)

    return ' '.join(format(byte, '02X') for byte in result)

def decrypt(hex_text, key):
    try:
        hex_values = [int(h, 16) for h in hex_text.split()]
    except ValueError:
        return "Error: Invalid hex input for decryption"

    result = []
    for i in range(0, len(hex_values), 8):
        block = hex_values[i:i+8]
        decrypted_block = ''.join(chr(b ^ ord(k)) for b, k in zip(block, key))
        result.append(decrypted_block)

    return remove_padding(''.join(result))

def encrypt_decrypt(text, key, operation):
    if len(key) != 8:
        return "Error: Key must be exactly 8 characters"
    if operation == 'encrypt':
        return encrypt(text, key)
    elif operation == 'decrypt':
        return decrypt(text, key)
    else:
        return "Error: Invalid operation. Use 'encrypt' or 'decrypt'"
