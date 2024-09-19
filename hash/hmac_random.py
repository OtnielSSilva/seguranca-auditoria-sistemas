"""
Um HMAC é uma construção que combina uma função hash com uma chave secreta.
"""

import hmac
import hashlib
from n_random import generate_random_bytes
from cifra_cesar import cifracesar

# Gera o HMAC para a mensagem fornecida usando a chave em hexadecimal.


def hmac_auth(key_hex, message):
    # Converte a chave de hexadecimal para bytes
    key_bytes = bytes.fromhex(key_hex)
    # Converte a mensagem de string para bytes
    message_bytes = message.encode('utf-8')
    # Cria o HMAC usando SHA-256 e retorna em hexadecimal
    return hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()

# Verifica se um HMAC fornecido é válido.


def verify_hmac(key_hex, message, hmac_to_verify):
    # Gera o HMAC a partir da chave e mensagem fornecidas
    generated_hmac = hmac_auth(key_hex, message)
    # Compara os HMACs de forma segura
    return hmac.compare_digest(generated_hmac, hmac_to_verify)


if __name__ == '__main__':
    # Exemplo de uso

    # Gera uma chave secreta de 16 bytes e converte para hexadecimal
    key = generate_random_bytes(16)
    key_cifra_cesar = 13
    # Cifra a mensagem usando a cifra de César
    message = cifracesar("mensagem_confidencial", key_cifra_cesar)

    print(f"Mensagem cifrada: {message}")

    # Gera o HMAC da mensagem cifrada
    hmac_value = hmac_auth(key, message)
    hmac_to_verify = hmac_value

    # Verifica se o HMAC gerado é válido
    is_valid = verify_hmac(key, message, hmac_to_verify)

    print(f"O HMAC é válido? {is_valid}")
