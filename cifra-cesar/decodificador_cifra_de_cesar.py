def decifra_cesar(texto, chave):
    resultado = ""
    chave = chave % 26  # prevenção em caso de chave > 26

    # iterando o texto
    for i in range(len(texto)):
        char = texto[i]

        # letras minúsculas
        if char.isupper():
            resultado += chr((ord(char) - 65 - chave) % 26 + 65)

        # letras maiúsculas
        elif char.islower():
            resultado += chr((ord(char) - 97 - chave) % 26 + 97)

        # outros caracteres
        else:
            resultado += char
    return resultado


def main():
    while True:
        meuTexto = input("Digite o texto: ")
        chave = int(input("Digite a chave: "))
        print("Texto decifrado: ", decifra_cesar(meuTexto, chave))

        while True:
            continuar = input("Deseja cifrar outro texto? (s/n): ").lower()
            if continuar == 's':
                break
            elif continuar == 'n':
                print("Encerrando o programa.")
                return
            else:
                print(
                    "Resposta inválida! Por favor, digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    main()
