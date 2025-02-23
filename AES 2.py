from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to encrypt a binary file using AES in CBC mode
def encrypt_file_AES_CBC(input_file, output_encrypted_file, key, iv):
    with open(input_file, 'rb') as file:
        data = file.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_encrypted_file, 'wb') as file:
        file.write(ciphertext)

# Function to decrypt a binary file using AES in CBC mode
def decrypt_file_AES_CBC(input_encrypted_file, output_decrypted_file, key, iv):
    with open(input_encrypted_file, 'rb') as file:
        ciphertext = file.read()

    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(output_decrypted_file, 'wb') as file:
        file.write(unpadded_data)

# Usage example
key = b'MySuperSecretKey2222222222222222'
iv = b'MySuperSecretIV0'
input_file = 'calc.exe'
output_encrypted_file = 'encrypted_output.txt'
output_decrypted_file = 'mycalc.exe'

# Encrypt the input file
encrypt_file_AES_CBC(input_file, output_encrypted_file, key, iv)
print(f'File {input_file} encrypted and saved as {output_encrypted_file}.')

# Decrypt the encrypted file
decrypt_file_AES_CBC(output_encrypted_file, output_decrypted_file, key, iv)
print(f'File {output_encrypted_file} decrypted and saved as {output_decrypted_file}.')