import hashlib

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Input the online hash here
online_hash = input("Enter the online SHA-256 hash: ")

file_path = "text.txt"

# Calculate the file hash
file_hash = calculate_sha256(file_path)

print(f"Calculated SHA-256 Hash: {file_hash}")
print(f"Online SHA-256 Hash: {online_hash}")

# Compare the hashes
if file_hash == online_hash:
    print("Hashes match. Verification successful.")
else:
    print("Hashes do not match. Verification failed.")
