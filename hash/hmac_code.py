"""
Um HMAC é uma construção que combina uma função hash com uma chave secreta.
"""

import hmac
import hashlib

# Gera o HMAC para uma mensagem usando uma chave secreta.


def hmac_auth(key, message):
    # Converte a chave de string para bytes
    key_bytes = key.encode('utf-8')
    # Converte a mensagem de string para bytes
    message_bytes = message.encode('utf-8')
    # Cria o HMAC usando SHA-256 e retorna em hexadecimal
    return hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()

# Verifica se um HMAC fornecido é válido.


def verify_hmac(key, message, hmac_to_verify):
    # Gera o HMAC a partir da chave e mensagem fornecidas.
    generated_hmac = hmac_auth(key, message)
    # Compara os HMACs de forma segura
    return hmac.compare_digest(generated_hmac, hmac_to_verify)


if __name__ == '__main__':
    # Exemplo de uso

    key = "chave_secreta"
    message = "mensagem_confidencial"

    # Corrigido erro de digitação: 'hmec_value' -> 'hmac_value'
    hmac_value = hmac_auth(key, message)
    hmac_to_verify = hmac_value

    # Verifica se o HMAC gerado é válido
    is_valid = verify_hmac(key, message, hmac_to_verify)

    print(f"O HMAC é válido? {is_valid}")
