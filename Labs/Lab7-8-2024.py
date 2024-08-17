# __________________________________________Task - 1_______________________________________________


# H(A) = 1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff

# H(B) = 6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c

# H(C) = c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781ba

# H(D) = b349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61

# H(X)=H(H(A)+H(B)) = 36b3575b009ec350c4d011e3b507c16d160f6132461e2b0f5e6e871f4b20aac6

# H(Y)=H(H(C)+H(D)) = 506c38b56f9c677348686dbe37c26f514bcdda19415a2563c00d651b8869e2cd

# Merkle Root = H(H(X)+H(Y)) = 9d0352d3aed678d1f4e992d575844509ad6bd8413b4e91acba005e50a64bab30




# __________________________________________Task - 2_______________________________________________





# import hashlib

# def hash_function(data):
#     return hashlib.sha256(data.encode()).hexdigest()

# def build_merkle_tree(hashes):
#     if len(hashes) == 1:
#         return hashes[0]
    
#     new_level = []
#     for i in range(0, len(hashes), 2):
#         left = hashes[i]
#         right = hashes[i + 1] if i + 1 < len(hashes) else left
#         combined = left + right
#         new_hash = hash_function(combined)
#         new_level.append(new_hash)
    
#     return build_merkle_tree(new_level)

# random_strings = [
#     "Muhammad",
#     "Ali",
#     "Fathima",
#     "Hussan",
#     "Hussain",
#     "Zahra",
#     "Baqar",
#     "Kazim"
# ]

# hashes = [hash_function(s) for s in random_strings]

# merkle_root = build_merkle_tree(hashes)

# print(f"Merkle Root: {merkle_root}")








# __________________________________________Task - 3_______________________________________________



# import hashlib

# def hash_function(data):
#     return hashlib.sha256(data.encode()).hexdigest()

# def build_merkle_tree(hashes):
#     while len(hashes) > 1:
#         new_level = []
#         for i in range(0, len(hashes), 2):
#             left = hashes[i]
#             right = hashes[i + 1] if i + 1 < len(hashes) else left
#             combined = left + right
#             new_hash = hash_function(combined)
#             new_level.append(new_hash)
#         hashes = new_level
#     return hashes[0]

# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# def split_into_blocks(data, num_blocks):
#     block_size = len(data) // num_blocks
#     blocks = [data[i * block_size:(i + 1) * block_size] for i in range(num_blocks)]
#     return blocks

# file_path = 'my_file.txt'

# file_content = read_file(file_path)

# blocks = split_into_blocks(file_content, 8)

# hashes = [hash_function(block) for block in blocks]

# merkle_root = build_merkle_tree(hashes)

# print(f"Merkle Root: {merkle_root}")



# __________________________________________Task - 4_______________________________________________



import hashlib

file_path = 'my_file.txt'

def hash_function(data):
    return hashlib.sha256(data.encode()).hexdigest()

def concat_and_hash(left, right):
    combined = left + right
    return hash_function(combined)

def build_merkle_tree(hashes):
    while len(hashes) > 1:
        new_level = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i + 1] if i + 1 < len(hashes) else left
            new_hash = concat_and_hash(left, right)
            new_level.append(new_hash)
        hashes = new_level
    return hashes[0]

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def split_into_blocks(data, num_blocks):
    block_size = len(data) // num_blocks
    blocks = [data[i * block_size:(i + 1) * block_size] for i in range(num_blocks)]
    return blocks



file_content = read_file(file_path)

blocks = split_into_blocks(file_content, 1024)

hashes = [hash_function(block) for block in blocks]

merkle_root = build_merkle_tree(hashes)

print(f"Merkle Root Hash ________ : {merkle_root}")
