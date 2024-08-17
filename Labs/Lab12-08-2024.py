from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

message = b"Hello, this is a test message!"

print("RSA Operations")

rsa_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
rsa_public_key = rsa_private_key.public_key()

encrypted_message = rsa_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = rsa_private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"Decrypted message: {decrypted_message}")

print("\nDSA Operations___________________________________________________")

dsa_private_key = dsa.generate_private_key(
    key_size=2048
)
dsa_public_key = dsa_private_key.public_key()

signature = dsa_private_key.sign(
    message,
    hashes.SHA256()
)
print(f"Signature: {signature}")

try:
    dsa_public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    is_valid = True
except:
    is_valid = False

print(f"Signature valid: {is_valid}")





# ____________________________________________________4th-Task______________________________________________________________




from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def generate_ecdsa_key_pair():
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key, public_key

def ecdsa_sign(private_key, message):
    signature = private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def ecdsa_verify(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False

def main():
    ecdsa_private_key, ecdsa_public_key = generate_ecdsa_key_pair()

    message = b"Message for ECDSA algorithm"

    signature = ecdsa_sign(ecdsa_private_key, message)

    verified = ecdsa_verify(ecdsa_public_key, message, signature)

    print("ECDSA:")
    print("ECDSA Public Key:", ecdsa_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode())
    print("ECDSA Private Key:", ecdsa_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode())
    print("Message:", message.decode())
    print("Signature:", signature.hex())
    print("Verification:", verified)

if __name__ == "__main__":
    main()
