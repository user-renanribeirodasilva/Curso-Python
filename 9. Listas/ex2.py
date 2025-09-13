# -*- coding: utf-8 -*-

"""
**Listas - Exercício 2: Sorteador da Mega-Sena v2.0 (Sem Repetição)**

**Objetivo:**
Aprimorar o nosso sorteador de números da Mega-Sena para garantir que ele gere 6 números **únicos**, sem repetições, utilizando uma lista para armazenar e verificar os números.

**Regras:**
1. Primeiro, importe o módulo `random`.
2. Crie uma lista vazia chamada `numeros_sorteados`.
3. Use um laço `while`. A condição do laço deve ser: "continue rodando enquanto o **tamanho da lista** for menor que 6". (Dica: `len(minha_lista)`).
4. Dentro do laço, a cada repetição:
   a. Sorteie um número inteiro entre 1 e 60.
   b. **A verificação principal:** Use um `if` para verificar se o número sorteado **NÃO** está na lista `numeros_sorteados`. A sintaxe para isso é: `if numero_sorteado not in numeros_sorteados:`.
   c. Se a condição for verdadeira (ou seja, o número é novo e não está na lista), adicione-o à lista com `.append()`.
5. **Após o laço `while` terminar** (o que só acontecerá quando a lista tiver 6 números), imprima a lista final de forma organizada.

**Entrada:**
- Nenhuma.

**Saída:**
- Os 6 números únicos sorteados.

**Exemplo de Execução:**

Sorteando 6 números únicos entre 1 e 60...
--------------------
Os números sorteados foram: [7, 15, 22, 31, 45, 58]

**Tópicos Praticados:**
- Criação e manipulação de Listas
- `.append()`
- `len()`
- Verificação de existência com o operador `in` (`not in`)
- Módulo `random`
- Laço `while`
"""

# --- Início do seu código ---
import random

numeros_sorteados = []

while len(numeros_sorteados) < 6:
    numero_sorteado = random.randint(1, 60)

    if numero_sorteado not in numeros_sorteados:
        numeros_sorteados.append(numero_sorteado)
print(f'Os números sorteados foram: {numeros_sorteados}')


# --- Fim do seu código ---