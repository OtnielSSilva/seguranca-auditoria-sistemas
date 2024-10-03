from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Função para gerar chave RSA (assimétrica)


def gerar_chaves():
    # Gerar chave privada e pública com RSA
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Gerar chave pública a partir da chave privada
    chave_publica = chave_privada.public_key()

    # Retornar as chaves
    return chave_privada, chave_publica

# Função para cifrar a mensagem com RSA


def cifra_mensagem(mensagem, chave_publica):
    # Codificar a mensagem para bytes
    mensagem_bytes = mensagem.encode('utf-8')

    # Cifrar a mensagem com a chave pública usando OAEP e SHA256
    mensagem_cifrada = chave_publica.encrypt(
        mensagem_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Retornar a mensagem cifrada
    return mensagem_cifrada

# Função para decifrar a mensagem com RSA


def decifrar_mensagem(mensagem_cifrada, chave_privada):
    # Decifrar a mensagem com a chave privada usando OAEP e SHA256
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Retornar a mensagem decifrada
    return mensagem_decifrada.decode('utf-8')

# Exemplo


# Gerar chaves
chave_privada, chave_publica = gerar_chaves()

mensagem = 'Mensagem secreta'

# Cifrar a mensagem com a chave pública
mensagem_cifrada = cifra_mensagem(mensagem, chave_publica)

# Decifrar a mensagem com a chave privada
mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave_privada)

# Exibir a mensagem cifrada e decifrada
print(f'Mensagem cifrada: {mensagem_cifrada}')
print(f'Mensagem decifrada: {mensagem_decifrada}')
