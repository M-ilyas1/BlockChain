# ____________________________________________Task - 1_____________________________________________________


from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

def rsa_encrypt_decrypt(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

    return encrypted_message, decrypted_message.decode()

def dsa_sign_verify(message):
    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    signature = private_key.sign(
        message.encode(),
        hashes.SHA256()
    )

    try:
        public_key.verify(
            signature,
            message.encode(),
            hashes.SHA256()
        )
        verification = True
    except:
        verification = False

    return signature, verification

def main():
    message = "This is a secret message"

    encrypted_message, decrypted_message = rsa_encrypt_decrypt(message)
    print(f"Original Message: {message}")
    print("__________________________________________________________________________________________________")

    print(f"Encrypted Message: {encrypted_message}")
    print("__________________________________________________________________________________________________")

    print(f"Decrypted Message: {decrypted_message}")
    print("__________________________________________________________________________________________________")


    signature, verification = dsa_sign_verify(message)
    print(f"Signature: {signature}")
    print("__________________________________________________________________________________________________")

    print(f"Signature Verified: {verification}")

if __name__ == "__main__":
    main()




