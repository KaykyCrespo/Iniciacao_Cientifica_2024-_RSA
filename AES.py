from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Função para criptografar um texto usando AES no modo CBC
def encrypt_AES_CBC(data, key, iv):
    # Criando um padder para garantir que o texto seja múltiplo do tamanho do bloco AES (16 bytes)
    padder = padding.PKCS7(128).padder()  # 128 bits = 16 bytes
    padded_data = padder.update(data.encode('utf-8'))  # Adiciona padding ao texto
    padded_data += padder.finalize()  # Finaliza o padding

    # Criando o objeto de cifra AES no modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()  # Criando o encriptador
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()  # Criptografando os dados

    return ciphertext  # Retorna o texto cifrado

# Função para descriptografar um texto cifrado usando AES no modo CBC
def decrypt_AES_CBC(ciphertext, key, iv):
    # Criando o objeto de cifra AES no modo CBC para descriptografia
    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()  # Descriptografando os dados

    # Removendo o padding para recuperar o texto original
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data)
    unpadded_data += unpadder.finalize()

    return unpadded_data.decode('utf-8')  # Retorna o texto descriptografado

# Exemplo de uso
key = b'MySuperSecretKey2222222222222222'  # Chave de criptografia (deve ter 16, 24 ou 32 bytes para AES-128, AES-192 ou AES-256)
iv = b'MySuperSecretIV0'  # Vetor de Inicialização (IV) deve ter 16 bytes
plaintext = "teste teste teste"  # Texto a ser criptografado

# Criptografando o texto
encrypted_text = encrypt_AES_CBC(plaintext, key, iv)
print(f'Encrypted text: {encrypted_text}')  # Exibe o texto criptografado

# Descriptografando o texto
decrypted_text = decrypt_AES_CBC(encrypted_text, key, iv)
print(f'Decrypted text: {decrypted_text}')  # Exibe o texto original


"""
O modo CBC (Cipher Block Chaining) é um dos modos de operação do algoritmo de criptografia AES (Advanced Encryption Standard). Ele funciona dividindo o texto a ser criptografado em blocos e encadeando cada bloco ao anterior para aumentar a segurança.

🔹 Como funciona o CBC?
O primeiro bloco de texto é XOR (operado bit a bit) com um Vetor de Inicialização (IV).
Esse resultado é então criptografado com a chave AES, gerando o primeiro bloco cifrado.
O próximo bloco de texto puro é XOR com o bloco cifrado anterior antes de ser criptografado.
Esse processo continua até o último bloco.
💡 A principal característica do CBC é que cada bloco cifrado depende do anterior, tornando a criptografia mais segura contra ataques de análise de padrões.

🔹 Exemplo visual:
Suponha que temos dois blocos de texto puro: P1 e P2.

Primeiro bloco:
C1=AES_Encrypt(P1⊕IV,Chave)

Segundo bloco:
C2=AES_Encrypt(P2⊕C1,Chave)


Para descriptografar, basta inverter o processo:
Recuperar P1:
P1=AES_Decrypt(C1,Chave)⊕IV

Recuperar P2:
P2=AES_Decrypt(C2,Chave)⊕C1


🔹 Vantagens do CBC:
✅ Maior segurança comparado ao modo ECB (Electronic Codebook), pois um mesmo texto claro gera diferentes textos cifrados devido ao encadeamento.
✅ Dificulta ataques estatísticos, pois a saída de um bloco influencia a criptografia do próximo.

🔹 Desvantagens do CBC:
⚠️ Necessita de um Vetor de Inicialização (IV) único para cada criptografia. Se o IV for reutilizado, pode comprometer a segurança.
⚠️ O processo de criptografia e descriptografia é sequencial, tornando-o menos eficiente para paralelização.

🚀 Resumo: O modo CBC torna a criptografia mais segura encadeando os blocos, mas exige um IV aleatório para cada operação.

"""