import random
import hashlib
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Function to generate SHA-256 hash of a randomly generated integer
def generateTxid():
    random_number = random.randint(1, 1000000)
    txid = hashlib.sha256(str(random_number).encode()).hexdigest()
    return txid

# Function to generate input for the transaction
def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0, 5)
    return prevTxid, prevOutputIndex

# Function to generate output for the transaction
def generateOutput():
    recipientAddress = 'recipient_address_' + str(random.randint(1, 100))
    amount = round(random.uniform(0.001, 1.0), 8)
    return recipientAddress, amount

# Function to generate a random transaction fee
def generateTransactionFee():
    transactionFee = round(random.uniform(0.0001, 0.001), 8)
    return transactionFee

# Function to generate a random transaction
def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex = generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee

# Function to concatenate all transaction details into a single string
def concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee):
    transactionData = (str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + 
                       str(outputRecipientAddress) + str(outputAmount) + str(transactionFee))
    return transactionData

# Function to generate an ECDSA key pair
def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey, ECDSAPublicKey

# Function to sign the transaction using ECDSA
def ECDSASign(privateKey, message):
    signature = privateKey.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature

# Function to verify the ECDSA signature
def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False

# Main function
def main():
    # Step 1: Generate random transaction details
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()

    # Step 2: Concatenate transaction details into a string and hash it
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).digest()

    # Step 3: Generate ECDSA key pair
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()

    # Step 4: Sign the transaction hash using the private key
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)

    # Step 5: Verify the signature using the public key
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)

    # Step 6: Print all the results
    print("\n=== ECDSA Transaction Signing ===")
    print("ECDSA Public Key:", ECDSAPublicKey.public_numbers())
    print("ECDSA Private Key:", ECDSAPrivateKey.private_numbers())
    print("Transaction Data (SHA-256 Hashed):", transactionDataAsMessageSHA256Hashed.hex())
    print("Signature:", signature.hex())
    print("Signature Verification:", verified)

# Call the main function
if __name__ == "__main__":
    main()
