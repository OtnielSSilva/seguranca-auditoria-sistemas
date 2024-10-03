from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from assinatura import assinar_mensagem, verificar_assinatura
from cifracao import cifra_mensagem, decifrar_mensagem, gerar_chaves

# Função para cifrar a mensagem com AES
def cifra_simetrica(mensagem, chave_simetrica):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(chave_simetrica), modes.CFB(iv))
    encryptor = cipher.encryptor()
    mensagem_cifrada = encryptor.update(mensagem) + encryptor.finalize()
    return iv + mensagem_cifrada

# Função para decifrar a mensagem com AES
def decifra_simetrica(mensagem_cifrada, chave_simetrica):
    iv = mensagem_cifrada[:16]
    cipher = Cipher(algorithms.AES(chave_simetrica), modes.CFB(iv))
    decryptor = cipher.decryptor()
    mensagem_decifrada = decryptor.update(mensagem_cifrada[16:]) + decryptor.finalize()
    return mensagem_decifrada

# Implementação do envelope criptográfico
def envelope_criptografico(mensagem, chave_publica_destinatario, chave_privada_remetente):
    chave_simetrica = os.urandom(32)  # Gera chave simétrica aleatória

    # Cifra a mensagem com a chave simétrica (AES)
    mensagem_cifrada = cifra_simetrica(mensagem.encode('utf-8'), chave_simetrica)

    # Cifra a chave simétrica com a chave pública do destinatário (RSA)
    chave_simetrica_cifrada = cifra_mensagem(chave_simetrica.hex(), chave_publica_destinatario)

    # Assina a mensagem 
    assinatura = assinar_mensagem(mensagem.encode('utf-8'), chave_privada_remetente)

    return mensagem_cifrada, chave_simetrica_cifrada, assinatura

# Função para abrir o envelope criptográfico
def abrir_envelope(mensagem_cifrada, chave_simetrica_cifrada, assinatura, chave_privada_destinatario, chave_publica_remetente):
    # Decifra a chave simétrica (RSA)
    chave_simetrica = bytes.fromhex(decifrar_mensagem(chave_simetrica_cifrada, chave_privada_destinatario))

    # Decifra a mensagem com a chave simétrica (AES)
    mensagem_decifrada = decifra_simetrica(mensagem_cifrada, chave_simetrica)

    # Verifica a assinatura 
    verificacao = verificar_assinatura(mensagem_decifrada, chave_publica_remetente, assinatura)

    # Retorna a mensagem decifrada e se a assinatura é válida
    return mensagem_decifrada.decode('utf-8'), verificacao

# Gerar chaves do remetente e destinatário
chave_privada_remetente, chave_publica_remetente = gerar_chaves()
chave_privada_destinatario, chave_publica_destinatario = gerar_chaves()

# Mensagem a ser enviada
mensagem = "Esta é uma mensagem secreta e assinada."

# Remetente cria o envelope criptográfico
mensagem_cifrada, chave_simetrica_cifrada, assinatura = envelope_criptografico(
    mensagem, chave_publica_destinatario, chave_privada_remetente
)

# Destinatário abre o envelope criptográfico
mensagem_decifrada, assinatura_valida = abrir_envelope(
    mensagem_cifrada, chave_simetrica_cifrada, assinatura, chave_privada_destinatario, chave_publica_remetente
)

# Exibir a mensagem decifrada e se a assinatura é válida
print(f"Mensagem decifrada: {mensagem_decifrada}")
print(f"Assinatura válida: {assinatura_valida}")
