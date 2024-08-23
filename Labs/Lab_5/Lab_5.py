# hash_functions.py

import hashlib
import bcrypt
import requests

# Function to hash text with various algorithms
def hash_text(text):
    text_bytes = text.encode()

    # Generate MD5 hash
    md5_hash = hashlib.md5(text_bytes).hexdigest()
    print("MD5 Hash:", md5_hash)

    # Generate SHA-1 hash
    sha1_hash = hashlib.sha1(text_bytes).hexdigest()
    print("SHA-1 Hash:", sha1_hash)

    # Generate SHA-256 hash
    sha256_hash = hashlib.sha256(text_bytes).hexdigest()
    print("SHA-256 Hash:", sha256_hash)

    # Generate SHA-512 hash
    sha512_hash = hashlib.sha512(text_bytes).hexdigest()
    print("SHA-512 Hash:", sha512_hash)

    # Generate BLAKE2 hash
    blake2_hash = hashlib.blake2b(text_bytes).hexdigest()
    print("BLAKE2 Hash:", blake2_hash)

    # Generate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', text_bytes).hexdigest()
    print("RIPEMD-160 Hash:", ripemd160_hash)

    # Generate bcrypt hash
    salt = bcrypt.gensalt()
    bcrypt_hash = bcrypt.hashpw(text_bytes, salt)
    print("bcrypt Hash:", bcrypt_hash.decode())

# Hash your name
name = input("Enter your name: ")
hash_text(name)

# Fetch and hash article content
url = "https://thefinancialexpress.com.bd/views/reviews/silicon-valleybanks-collapse-what-happened-and-why-it-matters"
response = requests.get(url)
article_text = response.text

print("\nHashing the article content:")
hash_text(article_text)

# Demonstrate avalanche effect by modifying the article
modified_article_text = article_text.replace("Silicon Valley Bank", "SVB")  # Example modification

print("\nHashing the modified article content:")
hash_text(modified_article_text)
