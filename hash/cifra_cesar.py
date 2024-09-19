def cifracesar(texto, chave):
    resultado = ""
    chave = chave % 26  # prevenção em caso de chave > 26

    # iterando o texto
    for i in range(len(texto)):
        char = texto[i]

        # letras minúsculas
        if char.isupper():
            resultado += chr((ord(char) - 65 + chave) % 26 + 65)

        # letras maiúsculas
        elif char.islower():
            resultado += chr((ord(char) - 97 + chave) % 26 + 97)

        # outros caracteres
        else:
            resultado += char
    return resultado
