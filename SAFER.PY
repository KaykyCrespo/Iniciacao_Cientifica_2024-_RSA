from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import constant_time
from cryptography.hazmat.backends import default_backend
import os

# Função para gerar chave a partir de uma senha
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return kdf.derive(password.encode())

# Função para criptografar dados
def encrypt_aes(data: bytes, password: str) -> dict:
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = generate_key(password, salt)

    # Padding dos dados para se alinhar ao bloco de 16 bytes
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Criação do cifrador AES no modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return {"ciphertext": ciphertext, "iv": iv, "salt": salt}

# Função para descriptografar dados
def decrypt_aes(encrypted_data: dict, password: str) -> bytes:
    salt = encrypted_data["salt"]
    iv = encrypted_data["iv"]
    ciphertext = encrypted_data["ciphertext"]
    key = generate_key(password, salt)

    # Criação do decifrador AES no modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Remover padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data

# Teste de criptografia e descriptografia
if __name__ == "__main__":
    original_data = b"Mensagem confidencial"
    password = "senha-segura"

    # Criptografia
    encrypted = encrypt_aes(original_data, password)
    print("Dados criptografados:", encrypted["ciphertext"])

    # Descriptografia
    decrypted = decrypt_aes(encrypted, password)
    print("Dados descriptografados:", decrypted.decode())
