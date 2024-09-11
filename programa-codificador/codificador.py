#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criado em: Wed Jul 12 15:17:37 XXXX

@author: eduardo
"""
# Encoder para imagens BMP

# Importando bibliotecas
from PIL import Image

# Função que converte uma string para binário usando codificação ASCII


def textToBinary(text):
    # Para cada caractere da string, converte para binário de 8 bits
    return ''.join((format(ord(i), 'b')).zfill(8) for i in text)

# Função principal (main)


def main():
    # Solicita ao usuário o nome do arquivo de imagem para abrir
    print('Digite o nome do arquivo de imagem para abrir:')
    imgIn = input()
    # Solicita o texto que será codificado na imagem
    print('Digite o texto a ser codificado:')
    textIn = input()
    # Solicita o nome do arquivo de imagem para gravar a saída
    print('Digite o nome do arquivo de imagem de saída:')
    imgOut = input()

    # Converte a mensagem do usuário para binário
    messageBin = textToBinary(textIn)

    try:
        # Tenta carregar os dados dos pixels da imagem
        img_pre = Image.open(imgIn)
        width, height = img_pre.size
        pixels = img_pre.load()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{imgIn}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    # Inicia o processo de alterar o bit menos significativo de cada pixel
    # para codificar a mensagem na imagem
    currBit = 0
    for x in range(0, width):
        # Se todos os bits da mensagem já foram codificados, para o loop
        if currBit >= len(messageBin):
            break

        # Obtém o pixel atual na posição (x, 0) da imagem
        currPix = pixels[x, 0]

        # Cria uma nova lista para o pixel com os valores RGB modificados
        newPix = list(currPix)
        for c in range(0, 3):
            # Se todos os bits da mensagem já foram codificados, para o loop
            if currBit >= len(messageBin):
                break
            # Converte o valor da cor para binário e altera o bit menos significativo
            colorBin = list(format(currPix[c], 'b').zfill(8))
            # Altera o último bit com o bit da mensagem
            colorBin[7] = messageBin[currBit]
            colorBin = ''.join(colorBin)
            newPix[c] = int(colorBin, 2)  # Converte de volta para decimal

            currBit += 1

        # Substitui o pixel antigo pelo novo pixel modificado
        currPix = tuple(newPix)
        pixels[x, 0] = currPix

    # Tenta salvar a imagem com os pixels modificados no arquivo de saída
    try:
        img_pre.save(imgOut)
        print(f"Imagem salva com sucesso em '{imgOut}'.")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")


# Chama a função principal
if __name__ == '__main__':
    main()
