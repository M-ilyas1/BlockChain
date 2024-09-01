from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

# RSA Key Pair Generation
def generateRSAKeyPair():
    privateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    publicKey = privateKey.public_key()
    return privateKey, publicKey

# RSA Encryption
def RSAEncrypt(publicKey, plainText):
    cipherText = publicKey.encrypt(
        plainText,
        padding.PKCS1v15()
    )
    return cipherText

# RSA Decryption
def RSADecrypt(privateKey, cipherText):
    plainText = privateKey.decrypt(
        cipherText,
        padding.PKCS1v15()
    )
    return plainText

# DSA Key Pair Generation
def generateDSAKeyPair():
    privateKey = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    publicKey = privateKey.public_key()
    return privateKey, publicKey

# DSA Signature Generation
def DSASign(privateKey, message):
    signature = privateKey.sign(
        message,
        hashes.SHA256()
    )
    return signature

# DSA Signature Verification
def DSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature,
            message,
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

# ECDSA Key Pair Generation
def generateECDSAKeyPair():
    privateKey = ec.generate_private_key(
        ec.SECP256K1(),
        backend=default_backend()
    )
    publicKey = privateKey.public_key()
    return privateKey, publicKey

# ECDSA Signature Generation
def ECDSASign(privateKey, message):
    signature = privateKey.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

# ECDSA Signature Verification
def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False

# Main function to demonstrate RSA, DSA, and ECDSA
def main():
    message = b"Message for cryptographic algorithms"

    # RSA Demonstration
    RSAprivateKey, RSApublicKey = generateRSAKeyPair()
    cipherText = RSAEncrypt(RSApublicKey, message)
    decryptedText = RSADecrypt(RSAprivateKey, cipherText)
    print("\n---RSA---")
    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", message.decode())
    print("Ciphertext:", cipherText)
    print("Decrypted Text:", decryptedText.decode())

    # DSA Demonstration
    DSAPrivateKey, DSAPublicKey = generateDSAKeyPair()
    signature = DSASign(DSAPrivateKey, message)
    verified = DSAVerify(DSAPublicKey, message, signature)
    print("\n---DSA---")
    print("DSA Public Key:", DSAPublicKey)
    print("DSA Private Key:", DSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

    # ECDSA Demonstration
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey, message)
    verified = ECDSAVerify(ECDSAPublicKey, message, signature)
    print("\n---ECDSA---")
    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key:", ECDSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

if __name__ == "__main__":
    main()
