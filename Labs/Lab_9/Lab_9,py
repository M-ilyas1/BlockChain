from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import utils

# RSA encryption and decryption
def rsa_encrypt_decrypt(message):
    # Generate RSA private and public keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Encrypt the message using the public key
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the ciphertext using the private key
    decrypted_message = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("\n---RSA Encryption and Decryption---")
    print("Ciphertext (encrypted message):", ciphertext)
    print("Decrypted message:", decrypted_message.decode())

# DSA signature generation and verification
def dsa_sign_verify(message):
    # Generate DSA private and public keys
    private_key = dsa.generate_private_key(
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Sign the message using the private key
    signature = private_key.sign(
        message.encode(),
        hashes.SHA256()
    )

    # Verify the signature using the public key
    try:
        public_key.verify(
            signature,
            message.encode(),
            hashes.SHA256()
        )
        print("\n---DSA Signature and Verification---")
        print("Signature:", signature)
        print("Signature is valid.")
    except Exception as e:
        print("Signature is invalid:", str(e))

# Main function to call RSA and DSA operations
def main():
    # Input plain text message
    message = input("Enter the plain text message: ")

    # RSA encryption and decryption
    rsa_encrypt_decrypt(message)

    # DSA signature generation and verification
    dsa_sign_verify(message)

# Run the main function
if __name__ == "__main__":
    main()
