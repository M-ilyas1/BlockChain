# import hashlib

# data = input("Enter the Text here__")

# hash_object = hashlib.sha256()

# hash_object.update(data.encode())

# hashed_data = hash_object.hexdigest()

# print("Hashed Data:", hashed_data)




# Hash of PDF file................................................................

# import hashlib

# pdf_path = 'Lab.pdf'
# algorithm = 'sha256'

# def hash_file(file_path, algorithm='sha256'):

#     hash_obj = hashlib.new(algorithm)
    
#     with open(file_path, 'rb') as file:
#         while chunk := file.read(8192):
#             hash_obj.update(chunk)
    
#     return hash_obj.hexdigest()

# hash_value = hash_file(pdf_path, algorithm)

# print(f'The {algorithm} hash of the file is: {hash_value}')



# Compare the hashes................................................................................

# online_hash = ""
# calculated_hash = "3194f08145c2c0822af5663e65dd35be59f73a121cff8b238c1b14467fdec048"


# if online_hash == calculated_hash:
#     print("The Hash matuches, Verification Success")
# else:
#     print("The Hash not matuches, Verification Failed")


# print("Online Hash :", online_hash)
# print("Calculted Hash :", calculated_hash)


# Create a text file with your own content..........................................................

import hashlib

text_file = "my_file.txt"
with open(text_file, "w") as f:
    f.write("This is Text file__")


txt_file_path = "my_file.txt"
txt_algorithm = 'sha256'

def hash_file(txt_file_path, algorithm='sha256'):

    hash_obj = hashlib.new(algorithm)
    
    with open(txt_file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    
    return hash_obj.hexdigest()

hash_value = hash_file(txt_file_path, txt_algorithm)

print(f'The {txt_algorithm} hash of the Txt_file is: {hash_value}')



# Downloade the manually to the same directory...............................

import hashlib

file_1 = "message1.bin"
file_2 = "message2.bin"

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def calculate_sha1(file_path):
    sha1_hash = hashlib.sha1()    
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()


file1_md5 = calculate_md5(file_1)
file2_md5 = calculate_md5(file_2)
file1_sha1 = calculate_sha1(file_1)
file2_sha1 = calculate_sha1(file_2)

print(f"File 1 MDS: {file1_md5}")
print(f"File 2 MDS: {file2_md5}")


