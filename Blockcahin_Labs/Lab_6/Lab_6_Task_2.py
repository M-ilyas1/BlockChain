# text_file_hash.py

import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Path to the text file
file_path = "text.txt"

# Calculate the original file hash
original_hash = calculate_sha256(file_path)
print(f"Original SHA-256 Hash: {original_hash}")

# Modify the file content
with open(file_path, "a") as file:
    file.write(" Adding some extra content to demonstrate avalanche effect.")

# Calculate the modified file hash
modified_hash = calculate_sha256(file_path)
print(f"Modified SHA-256 Hash: {modified_hash}")

# Demonstrate avalanche effect
if original_hash != modified_hash:
    print("Avalanche effect demonstrated: Hashes are different.")
else:
    print("No avalanche effect observed.")
