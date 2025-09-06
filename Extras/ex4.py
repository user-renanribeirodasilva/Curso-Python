# -*- coding: utf-8 -*-

"""
**Exercício 5 (Desafio Final do Módulo): FizzBuzz**

**Objetivo:**
Escrever um programa que imprima os números de 1 a 100 (inclusive), mas com três regras especiais:
1. Para números que são múltiplos de 3, em vez do número, imprima a palavra "Fizz".
2. Para números que são múltiplos de 5, em vez do número, imprima a palavra "Buzz".
3. Para números que são múltiplos de 3 e também de 5, em vez do número, imprima a palavra "FizzBuzz".

**Entrada:**
- Nenhuma entrada do usuário é necessária. O intervalo é fixo de 1 a 100.

**Saída:**
- A sequência de números e palavras, cada um em sua própria linha.
  O início da saída deve ser assim:
  1
  2
  Fizz
  4
  Buzz
  Fizz
  7
  8
  Fizz
  Buzz
  11
  Fizz
  13
  14
  FizzBuzz
  ... e assim por diante até 100.

**Dica Crucial:**
- A ordem das suas verificações no `if/elif/else` é MUITO importante. Pense bem: o que você deve verificar primeiro? Um número que é múltiplo de 3, de 5, ou de ambos?

**Tópicos Praticados:**
- Laço de Repetição (for e range)
- Operadores Aritméticos (%) e de Comparação (==)
- Operadores Lógicos (and)
- Desvios Condicionais (if, elif, else)
- Saída de dados (print)
"""

# --- Início do seu código ---

# 1. Crie um laço `for` que vá de 1 a 100. Lembre-se do `+1` no range.
for i in range (1, (100 + 1)):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    # 2. Dentro do laço, crie uma estrutura `if/elif/else` para testar as condições.
    #    Lembre-se da dica: qual é a condição mais específica que deve ser testada primeiro?


    # 3. Imprima o número ou a palavra correspondente em cada iteração do laço.


# --- Fim do seu código ---