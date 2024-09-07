import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Function to generate ECDSA public and private keys
def generate_ECDSA_key_pair():
    private_key = ec.generate_private_key(ec.SECP256K1())  # Generate private key using SECP256K1 curve
    public_key = private_key.public_key()  # Generate public key from private key
    return private_key, public_key

# Function to generate a Bitcoin address from the public key
def generate_bitcoin_address(public_key):
    # Convert the public key to bytes (Uncompressed format)
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    
    # Step 1: SHA-256 hash of the public key
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    
    # Step 2: RIPEMD-160 hash of the SHA-256 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    ripemd160_hash = ripemd160.digest()
    
    # Step 3: Add version byte (0x00 for mainnet addresses)
    versioned_payload = b'\x00' + ripemd160_hash
    
    # Step 4: Perform SHA-256 hash twice for checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    
    # Step 5: Add checksum to versioned payload
    full_payload = versioned_payload + checksum
    
    # Step 6: Convert to Base58 encoding
    bitcoin_address = base58.b58encode(full_payload)
    
    return bitcoin_address

# Main function to generate keys and Bitcoin address
def main():
    # Generate ECDSA key pair
    private_key, public_key = generate_ECDSA_key_pair()
    
    # Generate Bitcoin address
    bitcoin_address = generate_bitcoin_address(public_key)
    
    # Print keys and Bitcoin address
    print("Private Key:", private_key)
    print("Public Key:", public_key)
    print("Bitcoin Address:", bitcoin_address.decode())

# Run the main function
if __name__ == "__main__":
    main()
