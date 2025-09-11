# -*- coding: utf-8 -*-

"""
**Exercício 3: Triângulo Retângulo Alinhado à Direita**

**Objetivo:**
Escrever um programa que desenha um triângulo retângulo de altura N, mas desta vez, alinhado à direita.

**Entrada:**
- Um número inteiro positivo `N` fornecido pelo usuário.

**Saída:**
- Um padrão de asteriscos e espaços que forma um triângulo alinhado à direita.

**Exemplo:**
- Entrada: 5
  Saída:
    *
   **
  ***
 ****
*****

**Tópicos Praticados:**
- Laços Encadeados
- Coordenação de laços sequenciais dentro de um laço principal
"""

# --- Início do seu código ---

# Dicas para pensar:
# 1. Pense em cada linha como sendo composta de duas partes: um número de ESPAÇOS e depois um número de ASTERISCOS.
# 2. Isso significa que, dentro do seu laço de fora (que controla as linhas), você provavelmente precisará de DOIS laços internos, um depois do outro:
#    - Um primeiro laço interno para imprimir os espaços.
#    - Um segundo laço interno para imprimir os asteriscos.
# 3. Analise o padrão dos espaços e asteriscos para N=5:
#    - Linha 1 (i=1): 4 espaços, 1 asterisco
#    - Linha 2 (i=2): 3 espaços, 2 asteriscos
#    - Linha 3 (i=3): 2 espaços, 3 asteriscos
#    - Linha 4 (i=4): 1 espaço,  4 asteriscos
#    - Linha 5 (i=5): 0 espaços, 5 asteriscos
#
# Qual é a fórmula para a quantidade de espaços em relação a `N` e `i`?
# E a fórmula para a quantidade de asteriscos?

n = int(input('Digite um número: '))

# Seu código aqui...

for i in range (1, (n + 1)):
    for j in range (i):
        print('*', end=' ')
    print()


# --- Fim do seu código ---