import hashlib

def sha256(data):
    """Helper function to calculate SHA-256 hash of data."""
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_tree_hashes(data_blocks):
    """Construct a Merkle tree from data blocks and return the Merkle root."""
    current_level = [sha256(data) for data in data_blocks]
    
    # Continue creating higher levels until only one hash (root) remains
    while len(current_level) > 1:
        new_level = []
        for i in range(0, len(current_level), 2):
            # Combine pairs of hashes
            combined = current_level[i] + (current_level[i+1] if i+1 < len(current_level) else current_level[i])
            new_level.append(sha256(combined))
        current_level = new_level
    
    return current_level[0] if current_level else None

# Step 1: Define eight random strings
data_blocks = [
    "Muhammad",
    "Ali",
    "Fatima",
    "Hussain",
    "HUssain",
    "Zainab",
    "Kulsoom",
    "Zahra"
]

# Step 2: Calculate and print the Merkle root
merkle_root = merkle_tree_hashes(data_blocks)
print("Merkle Root of the tree:", merkle_root)
