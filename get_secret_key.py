# import os
# secret_key = os.urandom(24)
# print(secret_key)

########################################################

# # Generate 24 random bytes
# secret_key = os.urandom(24)

# # Convert the bytes into a readable format (like hexadecimal)
# print(secret_key.hex())

########################################################
import secrets
secret_key = secrets.token_bytes(24)
print(secret_key)