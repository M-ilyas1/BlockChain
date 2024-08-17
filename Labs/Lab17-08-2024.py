import base58
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

def generate_ecdsa_keys():
    # Generate ECDSA private key
    private_key = ec.generate_private_key(ec.SECP256K1())
    
    # Generate ECDSA public key
    public_key = private_key.public_key()
    
    return private_key, public_key

def public_key_to_address(public_key):
    # Convert public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint
    )
    
    # Perform SHA-256 hashing on the public key
    sha256 = hashlib.sha256(public_key_bytes).digest()
    
    # Perform RIPEMD-160 hashing on the result
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    
    # Add version byte in front (0x00 for mainnet)
    versioned_payload = b'\x00' + ripemd160
    
    # Perform SHA-256 hashing twice
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    
    # Append checksum to the end of versioned payload
    address_bytes = versioned_payload + checksum
    
    # Encode the address in base58
    address = base58.b58encode(address_bytes).decode('utf-8')
    
    return address

# Generate keys and wallet address
private_key, public_key = generate_ecdsa_keys()
bitcoin_address = public_key_to_address(public_key)

print(f'Private Key: {private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()).decode()}')
print(f'Public Key: {public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()}')
print(f'Bitcoin Address: {bitcoin_address}')
