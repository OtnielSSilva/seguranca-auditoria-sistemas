from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cifracao import gerar_chaves, cifra_mensagem, decifrar_mensagem

# Assinatura digital


def assinar_mensagem(mensagem, chave_privada):
    # Assinatura da mensagem com a chave privada usando PSS e SHA256
    assinatura = chave_privada.sign(
        mensagem,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    # Retornar a assinatura
    return assinatura

# Verificação da assinatura


def verificar_assinatura(mensagem, chave_publica, assinatura):
    # Tenta  da assinatura com a chave pública usando PSS e SHA256
    try:
        chave_publica.verify(assinatura, mensagem, padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                                               salt_length=padding.PSS.MAX_LENGTH),
                             hashes.SHA256())
        return True  # Assinatura válida
    except Exception as e:
        print("Vericação falhou: {e}")
        return False  # Assinatura inválida

# Exemplo


# Gerar chaves
chave_privada, chave_publica = gerar_chaves()

mensagem = 'Mensagem secreta'

# Converte a mensagem para bytes
mensagem_bytes = mensagem.encode('utf-8')

# Assinar a mensagem com a chave privada
assinatura = assinar_mensagem(mensagem_bytes, chave_privada)

# Verificar a assinatura com a chave pública
verificacao = verificar_assinatura(mensagem_bytes, chave_publica, assinatura)

# Exibir o resultado
if verificacao:
    print('Assinatura verificada com sucesso.')
else:
    print('Assinatura inválida')
