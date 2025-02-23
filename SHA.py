import hashlib

# Função para gerar um hash da senha utilizando SHA-256 e um salt
def hash_password(password, salt):
    password_hash = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return password_hash

# Função para verificar se a senha fornecida corresponde ao hash armazenado
def verify_password(stored_password, provided_password, salt):
    password_hash = hashlib.sha256((provided_password + salt).encode('utf-8')).hexdigest()
    return password_hash == stored_password

# Exemplo de uso:
user_password = "Your Password"  # Senha do usuário
provided_salt = "Your Salt"  # Substituir por um salt específico

# Gerar o hash da senha
hashed_password = hash_password(user_password, provided_salt)
print("Hashed Password:", hashed_password)

# Verificar uma senha
# SOMENTE TROCAS O Provided_password pelo valor que esta no user_password
provided_password = "Provided Password"  # Senha fornecida para verificação
password_matched = verify_password(hashed_password, provided_password, provided_salt)
print("Password Matched:", password_matched)


"""
Explicação

Importar hashlib - hashlib é uma biblioteca Python que fornece funções hash seguras. É usada aqui para hash SHA-256.


Função hash_password

Recebe uma senha em texto simples e um salt como entrada.
Concatena a senha e o salt.
Aplica a função de hash SHA-256 à string concatenada.
Converte o hash em uma representação hexadecimal.
Retorna a senha com hash.
Função verify_password

Recebe uma senha com hash armazenada, uma senha em texto simples fornecida e um salt como entrada.
Faz hash da senha fornecida usando o mesmo salt.
Compara o hash armazenado com o hash recém-calculado.
Retorna True se os hashes corresponderem, indicando uma verificação de senha bem-sucedida.
Exemplo de uso

Substitua "Sua senha" e "Seu salt" pela senha e pelo salt que você deseja usar.
Faça o hash da senha usando hash_password.
Imprima a senha com hash.
Verifique uma senha fornecida usando verify_password.
Imprima se a senha corresponde ou não.


Perguntas frequentes
P 1. Por que a segurança de senhas é importante na era digital?

Resposta. As senhas agem como a primeira linha de defesa contra acesso não autorizado a informações pessoais, tornando a segurança robusta crucial. Na era digital, onde as ameaças cibernéticas são prevalentes, práticas de senha seguras são essenciais para proteger dados confidenciais.

P 2. O que é hash e por que ele é usado na segurança de senhas?

Resposta. Hashing é um processo que transforma informações brutas em um formato irreversível, tornando desafiador fazer engenharia reversa. Na segurança de senhas, o hashing adiciona uma camada extra de proteção ao converter senhas em valores de hash exclusivos, evitando a exposição de senhas de texto simples.

P 3. O que é o algoritmo SHA-256?

Resposta. SHA-256, parte da família de algoritmos SHA-2, é uma função hash criptográfica. Ela produz uma saída de tamanho fixo de 256 bits, independentemente do tamanho da entrada. Conhecido por sua segurança, o SHA-256 é amplamente usado para fazer hash de senhas, tornando-as resistentes a vários ataques.

P 4. Por que o SHA-256 é considerado seguro?

Resposta. O SHA-256 é considerado seguro devido à sua resistência a ataques de colisão e pré-imagem. Seu tamanho de saída fixo garante segurança consistente e continua sendo uma escolha amplamente adotada para hash criptográfico em várias aplicações.

P 5. Qual é o propósito de adicionar sal ao hash de senha?

Resposta. Adicionar salt aumenta a segurança da senha ao introduzir aleatoriedade adicional ao processo de hash. Essa prática atenua vulnerabilidades associadas a hashes estáticos, como ataques de rainbow table. O salt de cada usuário garante saídas de hash exclusivas, mesmo para senhas idênticas.

P 6. Como o hash de senha salgada melhora a segurança?

Resposta. O hash de senha salted melhora a segurança ao dificultar que invasores usem tabelas pré-computadas (tabelas arco-íris) para quebrar senhas. O salt exclusivo para cada usuário garante que, mesmo que vários usuários tenham a mesma senha, suas senhas hashed serão diferentes.

P 7. Você pode explicar o código Python para fazer hash e verificar senhas?

Resposta. Certamente! O código Python fornecido usa a biblioteca hashlib para implementar hash SHA-256 com salt. Ele inclui funções para fazer hash de senhas (hash_password) e verificar senhas (verify_password). O uso de exemplo demonstra como fazer hash e verificar uma senha.

P 8. Como os desenvolvedores podem usar essas técnicas criptográficas para aumentar a segurança?

Resposta. Os desenvolvedores podem integrar essas técnicas em seus sistemas de autenticação. Ao usar algoritmos de hash criptográficos fortes como SHA-256 e incorporar salt, eles garantem um nível mais alto de segurança para senhas de usuários, protegendo informações confidenciais.

P 9. Que considerações devem ser levadas em consideração ao escolher um sal?

Resposta. Um salt deve ser criptograficamente seguro, aleatório e único para cada usuário. Usar um gerador aleatório seguro para criar salts garante imprevisibilidade e adiciona uma camada extra de proteção contra ataques potenciais.

P 10. Como a compreensão dessas técnicas criptográficas beneficia os desenvolvedores?

Resposta. Entender essas técnicas capacita os desenvolvedores a implementar medidas de segurança robustas, protegendo os dados do usuário contra acesso não autorizado. Ao se manterem informados sobre as melhores práticas criptográficas, os desenvolvedores contribuem para criar um ambiente digital mais seguro.
"""