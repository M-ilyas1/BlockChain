import hashlib

def sha256(data):
    """Calculate SHA-256 hash of the input data."""
    return hashlib.sha256(data).hexdigest()

def merkle_tree_hashes(data_blocks):
    """Construct a Merkle tree from data blocks and return the Merkle root."""
    current_level = [sha256(data) for data in data_blocks]
    
    while len(current_level) > 1:
        new_level = []
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + (current_level[i+1] if i+1 < len(current_level) else current_level[i])
            new_level.append(sha256(combined.encode()))
        current_level = new_level
    
    return current_level[0] if current_level else None

def read_file_in_blocks(file_path, block_size=1024):
    """Read a file and divide it into blocks of the specified size."""
    with open(file_path, 'rb') as file:
        while True:
            block = file.read(block_size)
            if not block:
                break
            yield block

# Import the file
file_path = "lecture_slides.pdf"  # Replace with your actual file path
data_blocks = list(read_file_in_blocks(file_path, block_size=1024))

# Ensure there are exactly 8 blocks
while len(data_blocks) < 8:
    data_blocks.append(data_blocks[-1])

# Calculate and print the Merkle root
merkle_root = merkle_tree_hashes(data_blocks)
print("Merkle Root of the file:", merkle_root)