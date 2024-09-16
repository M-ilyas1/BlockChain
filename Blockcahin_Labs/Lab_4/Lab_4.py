# Types of Hash Functions
# MD5:
# SHA-1:
# RIPEMD-160:
# bcrypt:
# SHA-256:
# SHA-512:
# BLAKE2:
# SHA-3:

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

print("Hash Function: MD5")
print("  Security:", hash_functions['MD5']['Security'])
print("  Collision Resistance:", hash_functions['MD5']['Collision Resistance'])
print("  Speed:", hash_functions['MD5']['Speed'])
print("  Output Size:", hash_functions['MD5']['Output Size'])
print("  Usage:", hash_functions['MD5']['Usage'])
print()

print("Hash Function: SHA-1")
print("  Security:", hash_functions['SHA-1']['Security'])
print("  Collision Resistance:", hash_functions['SHA-1']['Collision Resistance'])
print("  Speed:", hash_functions['SHA-1']['Speed'])
print("  Output Size:", hash_functions['SHA-1']['Output Size'])
print("  Usage:", hash_functions['SHA-1']['Usage'])
print()

print("Hash Function: RIPEMD-160")
print("  Security:", hash_functions['RIPEMD-160']['Security'])
print("  Collision Resistance:", hash_functions['RIPEMD-160']['Collision Resistance'])
print("  Speed:", hash_functions['RIPEMD-160']['Speed'])
print("  Output Size:", hash_functions['RIPEMD-160']['Output Size'])
print("  Usage:", hash_functions['RIPEMD-160']['Usage'])
print()

print("Hash Function: bcrypt")
print("  Security:", hash_functions['bcrypt']['Security'])
print("  Collision Resistance:", hash_functions['bcrypt']['Collision Resistance'])
print("  Speed:", hash_functions['bcrypt']['Speed'])
print("  Output Size:", hash_functions['bcrypt']['Output Size'])
print("  Usage:", hash_functions['bcrypt']['Usage'])
print()

print("Hash Function: SHA-256")
print("  Security:", hash_functions['SHA-256']['Security'])
print("  Collision Resistance:", hash_functions['SHA-256']['Collision Resistance'])
print("  Speed:", hash_functions['SHA-256']['Speed'])
print("  Output Size:", hash_functions['SHA-256']['Output Size'])
print("  Usage:", hash_functions['SHA-256']['Usage'])
print()

print("Hash Function: SHA-512")
print("  Security:", hash_functions['SHA-512']['Security'])
print("  Collision Resistance:", hash_functions['SHA-512']['Collision Resistance'])
print("  Speed:", hash_functions['SHA-512']['Speed'])
print("  Output Size:", hash_functions['SHA-512']['Output Size'])
print("  Usage:", hash_functions['SHA-512']['Usage'])
print()

print("Hash Function: BLAKE2")
print("  Security:", hash_functions['BLAKE2']['Security'])
print("  Collision Resistance:", hash_functions['BLAKE2']['Collision Resistance'])
print("  Speed:", hash_functions['BLAKE2']['Speed'])
print("  Output Size:", hash_functions['BLAKE2']['Output Size'])
print("  Usage:", hash_functions['BLAKE2']['Usage'])
print()

print("Hash Function: SHA-3")
print("  Security:", hash_functions['SHA-3']['Security'])
print("  Collision Resistance:", hash_functions['SHA-3']['Collision Resistance'])
print("  Speed:", hash_functions['SHA-3']['Speed'])
print("  Output Size:", hash_functions['SHA-3']['Output Size'])
print("  Usage:", hash_functions['SHA-3']['Usage'])
print()
