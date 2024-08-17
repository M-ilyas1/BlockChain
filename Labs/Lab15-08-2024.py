import hashlib
import random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate a random transaction ID
random_int = random.randint(1, 1000000)
txid = hashlib.sha256(str(random_int).encode()).hexdigest()

# Generate a previous transaction ID and output index
prev_txid = hashlib.sha256(str(random.randint(1, 1000000)).encode()).hexdigest()
prev_output_index = random.randint(0, 5)

# Generate a recipient address and amount
recipient_address = 'recipient_address_' + str(random.randint(1, 100))
amount = round(random.uniform(0.001, 1.0), 8)

# Generate a transaction fee
transaction_fee = round(random.uniform(0.0001, 0.001), 8)

# Concatenate all transaction details into a single string
transaction_data = (
    str(txid) + 
    str(prev_txid) + 
    str(prev_output_index) + 
    str(recipient_address) + 
    str(amount) + 
    str(transaction_fee)
)

# Convert transaction data to bytes and hash it using SHA-256
transaction_data_bytes = transaction_data.encode()
transaction_data_sha256_hashed = hashlib.sha256(transaction_data_bytes).digest()

# Generate ECDSA key pair
private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()

# Sign the hashed transaction data
signature = private_key.sign(
    transaction_data_sha256_hashed,
    ec.ECDSA(hashes.SHA256())
)

# Verify the signature
try:
    public_key.verify(
        signature,
        transaction_data_sha256_hashed,
        ec.ECDSA(hashes.SHA256())
    )
    verified = True
except:
    verified = False

# Print results
print("ECDSA:")
print("ECDSA Public Key (in bytes):", public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).hex())
print("ECDSA Private Key (in bytes):", private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).hex())
print("Transaction Data SHA-256 Hash:", transaction_data_sha256_hashed.hex())
print("Signature:", signature.hex())
print("Verification:", verified)
