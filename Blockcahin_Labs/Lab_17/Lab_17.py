import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Step 1: Generate ECDSA key pair
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# Step 2: Convert the public key to bytes (Uncompressed format)
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

# Step 3: Perform SHA-256 hash of the public key
sha256_hash = hashlib.sha256(public_key_bytes).digest()

# Step 4: Perform RIPEMD-160 hash of the SHA-256 hash
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256_hash)
ripemd160_hash = ripemd160.digest()

# Step 5: Add version byte (0x00 for mainnet addresses)
versioned_payload = b'\x00' + ripemd160_hash

# Step 6: Perform SHA-256 hash twice for checksum
checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

# Step 7: Add checksum to versioned payload
full_payload = versioned_payload + checksum

# Step 8: Convert to Base58 encoding for Bitcoin address
bitcoin_address = base58.b58encode(full_payload)

# Output the keys and Bitcoin address
print("Private Key:", private_key)
print("Public Key:", public_key)
print("Bitcoin Address:", bitcoin_address.decode())
