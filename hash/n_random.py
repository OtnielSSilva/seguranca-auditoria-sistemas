import os


def generate_random_bytes(length):
    # os.urandom(length) -> gera length bytes de dados aleatórios criptograficamente seguros.
    # .hex() -> converte os bytes gerados para uma representação hexadecimal.
    return os.urandom(length).hex()


def main():

    # Exemplo de uso
    random_value = generate_random_bytes(16)

    # 16 bytes aleatórios
    print(f"Numero Aleatorio: {random_value}")


if __name__ == '__main__':
    main()
