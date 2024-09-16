import hashlib
import bcrypt


def hash_text(text):
    text_bytes = text.encode()

    md5_hash = hashlib.md5(text_bytes).hexdigest()
    print("MD5 Hash:", md5_hash)

    sha1_hash = hashlib.sha1(text_bytes).hexdigest()
    print("SHA-1 Hash:", sha1_hash)

    sha256_hash = hashlib.sha256(text_bytes).hexdigest()
    print("SHA-256 Hash:", sha256_hash)

    sha512_hash = hashlib.sha512(text_bytes).hexdigest()
    print("SHA-512 Hash:", sha512_hash)

    blake2_hash = hashlib.blake2b(text_bytes).hexdigest()
    print("BLAKE2 Hash:", blake2_hash)

    ripemd160_hash = hashlib.new('ripemd160', text_bytes).hexdigest()
    print("RIPEMD-160 Hash:", ripemd160_hash)

    salt = bcrypt.gensalt()
    bcrypt_hash = bcrypt.hashpw(text_bytes, salt)
    
    print("bcrypt Hash:", bcrypt_hash.decode())


name = input("Enter your name: ")
hash_text(name)


