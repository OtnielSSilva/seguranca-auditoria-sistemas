#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Criado em: Wed Jul 12 15:54:26 XXXX

@author: eduardo
"""

# Decoder para imagens BMP

# Importando bibliotecas
from PIL import Image

# Função que converte uma string binária para texto usando codificação ASCII


def binaryToText(binStr):
    retStr = ''
    # Para cada conjunto de 8 bits, converte para o caractere correspondente
    for i in range(0, len(binStr) // 8):
        retStr += chr(int(binStr[i*8:i*8+8], 2))
    return retStr

# Função principal (main)


def main():
    # Solicita ao usuário o nome do arquivo de imagem para abrir
    print('Digite o nome da imagem para decodificar:')
    imgIn = input()
    # Solicita ao usuário o número de caracteres a serem decodificados
    print('Digite o número de caracteres a decodificar:')
    try:
        numChars = int(input())
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        return

    numBits = numChars * 8

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

    # Inicia o processo de decodificação dos bits menos significativos
    binStr = ''
    currBit = 0
    for x in range(0, width):
        # Se todos os bits necessários já foram lidos, para o loop
        if currBit >= numBits:
            break

        # Obtém o pixel atual na posição (x, 0) da imagem
        currPix = pixels[x, 0]

        # Coleta os bits menos significativos dos valores RGB
        for c in range(0, 3):
            if currBit >= numBits:
                break
            # Adiciona o bit menos significativo à string binária
            colorBin = list(format(currPix[c], 'b').zfill(8))
            binStr += colorBin[7]

            currBit += 1

    # Converte a string binária para texto e imprime o resultado
    print("Texto decodificado:")
    try:
        decodedText = binaryToText(binStr)
        print(decodedText)
    except Exception as e:
        print(f"Erro ao decodificar o texto: {e}")


# Chama a função principal
if __name__ == '__main__':
    main()
