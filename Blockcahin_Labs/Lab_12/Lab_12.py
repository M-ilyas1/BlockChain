from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

# Input message
message = b"Message for cryptographic algorithms"

# Generate RSA key pair
RSAprivateKey = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
RSApublicKey = RSAprivateKey.public_key()

# Encrypt the message using RSA public key
RSACipherText = RSApublicKey.encrypt(
    message,
    padding.PKCS1v15()
)

# Decrypt the ciphertext using RSA private key
RSADecryptedText = RSAprivateKey.decrypt(
    RSACipherText,
    padding.PKCS1v15()
)

print("\n---RSA---")
print("RSA Public Key:", RSApublicKey)
print("RSA Private Key:", RSAprivateKey)
print("Plaintext:", message.decode())
print("Ciphertext:", RSACipherText)
print("Decrypted Text:", RSADecryptedText.decode())


# Generate DSA key pair
DSAPrivateKey = dsa.generate_private_key(
    key_size=1024,
    backend=default_backend()
)
DSAPublicKey = DSAPrivateKey.public_key()

# Sign the message using DSA private key
DSASignature = DSAPrivateKey.sign(
    message,
    hashes.SHA256()
)

# Verify the DSA signature using the public key
try:
    DSAPublicKey.verify(
        DSASignature,
        message,
        hashes.SHA256()
    )
    DSA_Verified = True
except InvalidSignature:
    DSA_Verified = False

print("\n---DSA---")
print("DSA Public Key:", DSAPublicKey)
print("DSA Private Key:", DSAPrivateKey)
print("Message:", message.decode())
print("Signature:", DSASignature)
print("Verification:", DSA_Verified)

# Generate ECDSA key pair
ECDSAPrivateKey = ec.generate_private_key(
    ec.SECP256K1(),
    backend=default_backend()
)
ECDSAPublicKey = ECDSAPrivateKey.public_key()

# Sign the message using ECDSA private key
ECDSASignature = ECDSAPrivateKey.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Verify the ECDSA signature using the public key
try:
    ECDSAPublicKey.verify(
        ECDSASignature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    ECDSA_Verified = True
except InvalidSignature:
    ECDSA_Verified = False

print("\n---ECDSA---")
print("ECDSA Public Key:", ECDSAPublicKey)
print("ECDSA Private Key:", ECDSAPrivateKey)
print("Message:", message.decode())
print("Signature:", ECDSASignature)
print("Verification:", ECDSA_Verified)
