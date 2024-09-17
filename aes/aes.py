from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Função para encriptar uma mensagem usando AES


def aes_encriptar(mensagem, chave):
    # Gera um IV (vetor de inicialização) aleatório do tamanho do bloco AES
    iv = get_random_bytes(AES.block_size)
    # Cria um objeto de cifra AES no modo CBC, com a chave e o IV
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Adiciona padding à mensagem para que seu tamanho seja múltiplo do bloco AES
    mensagem_padded = pad(mensagem.encode("utf-8"), AES.block_size)
    # Encripta a mensagem com padding
    mensagem_encriptada = cipher.encrypt(mensagem_padded)

    # Retorna o IV concatenado com a mensagem encriptada
    return iv + mensagem_encriptada

# Função para decriptar uma mensagem encriptada usando AES


def aes_decriptar(mensagem_encriptada, chave):
    # Extrai o IV da mensagem encriptada (os primeiros bytes correspondem ao IV)
    iv = mensagem_encriptada[:AES.block_size]
    # Cria um objeto de cifra AES no modo CBC, com a chave e o IV
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    # Decripta a mensagem (omitindo o IV) e remove o padding
    mensagem_padded = cipher.decrypt(mensagem_encriptada[AES.block_size:])
    # Remove o padding da mensagem decriptada
    mensagem = unpad(mensagem_padded, AES.block_size)

    # Retorna a mensagem decriptada convertida de bytes para string
    return mensagem.decode("utf-8")


def menu():
    # Gera uma chave aleatória de 16 bytes
    chave = get_random_bytes(16)

    while True:
        print("\nSelecione uma opção:")
        print("1 - Encriptar mensagem")
        print("2 - Decriptar mensagem")
        print("0 - Sair")
        opcao = input("Opção: ")

        # Caso o usuário escolha encriptar uma mensagem
        if opcao == '1':
            mensagem = input("Digite a mensagem a ser encriptada: ")
            # Encripta a mensagem e armazena o resultado
            mensagem_encriptada = aes_encriptar(mensagem, chave)
            print(f"Mensagem encriptada: {mensagem_encriptada}")
        # Caso o usuário escolha decriptar a mensagem
        elif opcao == '2':
            mensagem = input("Digite a mensagem a ser decifrada: ")

            # Decripta e exibe a mensagem
            mensagem_decriptada = aes_decriptar(mensagem_encriptada, chave)
            print(f"Mensagem decriptada: {mensagem_decriptada}")

        elif opcao == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
