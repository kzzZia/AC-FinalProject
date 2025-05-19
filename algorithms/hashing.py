import hashlib

def hash_text(text, algo):
    return get_hash_func(algo)(text.encode()).hexdigest()

def hash_file(path, algo):
    hash_func = get_hash_func(algo)()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def get_hash_func(algo):
    return {
        "SHA256": hashlib.sha256,
        "SHA1": hashlib.sha1,
        "MD5": hashlib.md5,
        "BLAKE2": hashlib.blake2b,
    }[algo]
