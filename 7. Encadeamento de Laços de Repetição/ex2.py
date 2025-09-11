# -*- coding: utf-8 -*-

"""
**Exercício 2: Desenhando um Triângulo Retângulo Invertido**

**Objetivo:**
Escrever um programa que solicita ao usuário um número `N` e desenha um triângulo retângulo invertido de altura `N`.

**Entrada:**
- Um número inteiro positivo `N` fornecido pelo usuário.

**Saída:**
- Um padrão de asteriscos que forma um triângulo invertido. A primeira linha deve ter N asteriscos, a segunda N-1, e assim por diante, até a última linha que terá 1 asterisco.

**Exemplo:**
- Entrada: 5
  Saída:
  *****
  ****
  ***
  **
  *

**Tópicos Praticados:**
- Laços Encadeados
- Lógica com `range`
- Operadores Aritméticos
"""

# --- Início do seu código ---

# A estrutura básica é a mesma. O laço de fora ainda pode contar as linhas de 1 a N.
# A grande mudança está na lógica do `range` do laço de dentro.

# Dica para pensar:
# Na linha 1 (i=1), você precisa de N asteriscos.
# Na linha 2 (i=2), você precisa de N-1 asteriscos.
# Na linha 3 (i=3), você precisa de N-2 asteriscos.
# ...
# Na linha N (i=N), você precisa de 1 asterisco.

# Qual é a fórmula matemática que relaciona `i`, `N` e a quantidade de asteriscos que você precisa imprimir?
# O laço interno poderia ser algo como `for j in range( ...fórmula aqui... ):`

n = int(input('Digite um número: '))

# Seu código aqui...

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()



# --- Fim do seu código ---