# Python Basics Lab 4 - Hash Functions

# Introduction
# Hash functions are cryptographic tools that take an input (message) of arbitrary size
# and produce a fixed-length output (hash). The hash is unique to the input message.
# Any change in the input results in a different hash output. They are widely used in
# password storage, digital signatures, and other applications.

# Properties of Good Hash Function
# 1. Collision Resistance: It should be hard to find two different inputs that produce the same hash.
# 2. Pre-Image Resistance: Given a hash output, it should be hard to find the input message that produced it.
# 3. Avalanche Effect: A small change in input should result in a significant change in the hash output.

# Types of Hash Functions
# - MD5 (1992)
# - SHA-1 (1995)
# - RIPEMD-160 (1996)
# - bcrypt (1999)
# - SHA-256 (2001)
# - SHA-512 (2001)
# - BLAKE2 (2013)
# - SHA-3 (2015)

# MD5
# History: Developed by Ronald Rivest in 1991 as a successor to MD4. Was widely used until vulnerabilities
# were discovered in 2004.
# Characteristics: 128-bit hash function, fast and efficient, but weak collision resistance.
# Usage: Password storage, data integrity checks (e.g., Git).
# Vulnerabilities: Susceptible to collision and length extension attacks.

# SHA-1
# History: Developed by NSA and published in 1995. Widely used until vulnerabilities emerged in mid-2000s.
# Characteristics: 160-bit hash function, fast and efficient, but weak collision resistance.
# Usage: Digital signatures, data integrity checks (e.g., SSL/TLS, Git, SVN).
# Vulnerabilities: Vulnerable to collision attacks.

# RIPEMD-160
# History: Developed by European cryptographers in 1996 as a stronger alternative to earlier RIPEMD.
# Characteristics: 160-bit hash function, slower but more resistant to collision attacks than SHA-1.
# Usage: Cryptographic applications, Bitcoin protocol.
# Vulnerabilities: Less secure than SHA-256 and SHA-3, but attacks are not practical yet.

# bcrypt
# History: Developed by Niels Provos and David Mazières in 1999 for password hashing.
# Characteristics: Designed to be slow and computationally expensive, resistant to brute force attacks.
# Usage: Password storage (e.g., Facebook, Twitter, LinkedIn).
# Vulnerabilities: Strong but implementation and database security are crucial.

# SHA-256
# History: Developed by NSA and published in 2001 as part of SHA-2 family.
# Characteristics: 256-bit hash function, fast and efficient, better collision resistance than SHA-1.
# Usage: Digital signatures, message authentication codes, password hashing, Bitcoin protocol.
# Vulnerabilities: No practical collision attacks found; theoretical attacks exist.

# SHA-512
# History: Developed by NSA and published in 2001 as part of SHA-2 family.
# Characteristics: 512-bit hash function, fast and efficient, better collision resistance than SHA-384.
# Usage: Cryptographic applications, encryption.
# Vulnerabilities: No practical collision attacks found; theoretical attacks exist.

# BLAKE2
# History: Developed in 2013 as a faster and more efficient alternative to SHA-3.
# Characteristics: Variable-length hash function, faster and more efficient than SHA-3.
# Usage: Password hashing, digital signatures, Zcash cryptocurrency protocol.
# Vulnerabilities: Relatively new, less scrutiny compared to older hash functions.

# SHA-3
# History: Developed by NIST and published in 2015 as a replacement for SHA-2.
# Characteristics: Variable-length hash function, faster and more efficient than SHA-2.
# Usage: Cryptographic applications, encryption.
# Vulnerabilities: No practical attacks found; relatively new and less scrutinized.

# Comparison Table
hash_functions = {
    'MD5': {'Security': 'Less Secure', 'Collision Resistance': 'Not Collision-Resistant', 'Speed': 'Fast', 'Output Size': '128 bits', 'Usage': 'Legacy systems and applications'},
    'SHA-1': {'Security': 'Less Secure', 'Collision Resistance': 'Not Collision-Resistant', 'Speed': 'Fast', 'Output Size': '160 bits', 'Usage': 'Legacy systems and applications'},
    'RIPEMD-160': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Medium', 'Output Size': '160 bits', 'Usage': 'Cryptographic applications and protocols'},
    'bcrypt': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Slow', 'Output Size': 'Variable', 'Usage': 'Password storage'},
    'SHA-256': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Fast', 'Output Size': '256 bits', 'Usage': 'Cryptographic applications and protocols, including Bitcoin'},
    'SHA-512': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Fast', 'Output Size': '512 bits', 'Usage': 'Cryptographic applications and protocols, including encryption'},
    'BLAKE2': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Fast', 'Output Size': 'Variable', 'Usage': 'Password hashing, cryptocurrency mining'},
    'SHA-3': {'Security': 'Secure', 'Collision Resistance': 'Collision-Resistant', 'Speed': 'Fast', 'Output Size': 'Variable', 'Usage': 'Cryptographic applications and protocols, including encryption'}
}

# Print comparison
for func, attributes in hash_functions.items():
    print(f"Hash Function: {func}")
    for key, value in attributes.items():
        print(f"  {key}: {value}")
    print()

# Task
# You are required to do some online research on the following hashing algorithms and attempt the quiz
# from the link provided: https://forms.gle/bNF62VtpAJhTBabs7
