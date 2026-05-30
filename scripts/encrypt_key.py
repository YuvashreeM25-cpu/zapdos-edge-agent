from cryptography.fernet import Fernet

# 1. Generate and save a key (Do this once!)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# 2. Encrypt your API Key
cipher_suite = Fernet(key)
api_key = input("Enter your Gemini API Key: ").encode()
encrypted_key = cipher_suite.encrypt(api_key)

with open("encrypted_key.bin", "wb") as file:
    file.write(encrypted_key)

print("Key encrypted and saved to 'encrypted_key.bin'. Keep 'secret.key' safe!")