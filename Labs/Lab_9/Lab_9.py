from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils

# Input plain text message
message = input("Enter the plain text message: ").encode()

# Generate RSA private and public keys
rsa_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
rsa_public_key = rsa_private_key.public_key()

# Encrypt the message using the public key
rsa_ciphertext = rsa_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the ciphertext using the private key
rsa_decrypted_message = rsa_private_key.decrypt(
    rsa_ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\n---RSA Encryption and Decryption---")
print("Ciphertext (encrypted message):", rsa_ciphertext)
print("Decrypted message:", rsa_decrypted_message.decode())


# Generate DSA private and public keys
dsa_private_key = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)
dsa_public_key = dsa_private_key.public_key()

# Sign the message using the private key
dsa_signature = dsa_private_key.sign(
    message,
    hashes.SHA256()
)

# Verify the signature using the public key
try:
    dsa_public_key.verify(
        dsa_signature,
        message,
        hashes.SHA256()
    )
    print("\n---DSA Signature and Verification---")
    print("Signature:", dsa_signature)
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid:", str(e))
