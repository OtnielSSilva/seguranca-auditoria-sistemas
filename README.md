# Códigos e desafios desenvolvidos em laboratório na disciplina de Segurança e Auditoria de Sistemas

Este projeto implementa diferentes técnicas de criptografia para codificar e decodificar mensagens em imagens e realizar a criptografia de mensagens com algoritmos de segurança, como AES e Cifra de César, além de gerar hashes usando HMAC (e podendo gerar bytes aleatórios como chave).

## Funcionalidades

- **Codificação de mensagens em imagens**: Utiliza o bit menos significativo (LSB) para esconder mensagens em uma imagem.
- **Decodificação de mensagens de imagens**: Extrai mensagens codificadas em imagens.
- **Criptografia AES**: Implementa o algoritmo AES (Advanced Encryption Standard) para criptografar e descriptografar mensagens.
- **Cifra de César**: Uma implementação da Cifra de César para criptografia de mensagens simples.
- **Hashing com HMAC**: Gera hashes seguros usando HMAC (Hash-based Message Authentication Code).
- **Geração de bytes aleatórios**: Utiliza um gerador de números aleatórios seguro para a geração de bytes para uso em chaves criptográficas.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Bibliotecas**:
  - `PIL` para manipulação de imagens
  - `Crypto.Cipher` (AES), `Crypto.Util.Padding` e `Crypto.Random` para criptografia AES
    ```python
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Random import get_random_bytes
    ```
  - `hmac` e `hashlib` para geração de HMAC
    ```python
    import hmac
    import hashlib
    ```
  - `os` para geração de números aleatórios
    ```python
    import os
    ```

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/OtnielSSilva/seguranca-auditoria-sistemas.git
