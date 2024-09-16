# file_hashes.py

import hashlib

def calculate_hashes(file_path):
    """Calculate MD5 and SHA-1 hashes of a file."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            md5.update(chunk)
            sha1.update(chunk)
    return md5.hexdigest(), sha1.hexdigest()

# Paths to the downloaded files
file1_path = "message1.bin"
file2_path = "message2.bin"

# Calculate and print hashes for both files
md5_hash1, sha1_hash1 = calculate_hashes(file1_path)
md5_hash2, sha1_hash2 = calculate_hashes(file2_path)

print(f"Message1.bin - MD5: {md5_hash1}, SHA-1: {sha1_hash1}")
print(f"Message2.bin - MD5: {md5_hash2}, SHA-1: {sha1_hash2}")

# Describe findings
if md5_hash1 == md5_hash2:
    print("MD5 hashes of message1.bin and message2.bin are the same.")
else:
    print("MD5 hashes of message1.bin and message2.bin are different.")

if sha1_hash1 == sha1_hash2:
    print("SHA-1 hashes of message1.bin and message2.bin are the same.")
else:
    print("SHA-1 hashes of message1.bin and message2.bin are different.")
