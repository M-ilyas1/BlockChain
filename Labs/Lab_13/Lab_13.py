from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

# RSA Functions
def generateRSAKeyPair():
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    publicKey = privateKey.public_key()
    return privateKey, publicKey

def RSAEncrypt(publicKey, plainText):
    cipherText = publicKey.encrypt(
        plainText,
        padding.PKCS1v15()
    )
    return cipherText

def RSADecrypt(privateKey, cipherText):
    plainText = privateKey.decrypt(
        cipherText,
        padding.PKCS1v15()
    )
    return plainText

# DSA Functions
def generateDSAKeyPair():
    privateKey = dsa.generate_private_key(key_size=1024)
    publicKey = privateKey.public_key()
    return privateKey, publicKey

def DSASign(privateKey, message):
    signature = privateKey.sign(
        message,
        hashes.SHA256()
    )
    return signature

def DSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature,
            message,
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# ECDSA Functions
def generateECDSAKeyPair():
    privateKey = ec.generate_private_key(ec.SECP256K1())
    publicKey = privateKey.public_key()
    return privateKey, publicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception:
        return False

def main():
    # RSA Section
    print("\n=== RSA ===")
    RSAprivateKey, RSApublicKey = generateRSAKeyPair()
    message = b"Message for RSA algorithm"
    cipherText = RSAEncrypt(RSApublicKey, message)
    decryptedText = RSADecrypt(RSAprivateKey, cipherText)

    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", message.decode())
    print("Ciphertext:", cipherText)
    print("Decrypted Text:", decryptedText.decode())

    # DSA Section
    print("\n=== DSA ===")
    DSAPrivateKey, DSAPublicKey = generateDSAKeyPair()
    message = b"Message for DSA algorithm"
    signature = DSASign(DSAPrivateKey, message)
    verified = DSAVerify(DSAPublicKey, message, signature)

    print("DSA Public Key:", DSAPublicKey)
    print("DSA Private Key:", DSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

    # ECDSA Section
    print("\n=== ECDSA ===")
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    message = b"Message for ECDSA algorithm"
    signature = ECDSASign(ECDSAPrivateKey, message)
    verified = ECDSAVerify(ECDSAPublicKey, message, signature)

    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key:", ECDSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

if __name__ == "__main__":
    main()
