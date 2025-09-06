# -*- coding: utf-8 -*-

"""
**Exercício 1: Verificador de Números Primos**

**Objetivo:**
Escreva um programa que recebe um número inteiro do usuário e determina se ele é um número primo ou não.

**Definição:**
Um número primo é um número natural maior que 1 que tem apenas dois divisores distintos: o 1 e ele mesmo.

**Entrada:**
- Um número inteiro fornecido pelo usuário.

**Saída:**
- Se o número for primo, imprima: f"{numero} é um número primo."
- Se o número não for primo, imprima: f"{numero} não é um número primo."

**Exemplos:**
- Entrada: 7
  Saída: 7 é um número primo.
- Entrada: 10
  Saída: 10 não é um número primo.
- Entrada: 1
  Saída: 1 não é um número primo.
- Entrada: 2
  Saída: 2 é um número primo.

**Tópicos Praticados:**
- Variáveis e Tipos de Dados (int)
- Operadores Aritméticos (%)
- Operadores de Comparação (>, ==, <=)
- Operadores Lógicos (se necessário)
- Desvios Condicionais (if, elif, else)
- Laço de Repetição (for e range)
- Entrada de dados (input)
- Saída de dados (print com f-string)
"""

# --- Início do seu código ---

# 1. Solicite ao usuário que insira um número inteiro e armazene-o.
#    Lembre-se de converter a entrada, que é uma string, para um número inteiro.
entrada = int(input('Digite um número: '))


# 2. Crie a lógica para verificar se o número é primo.
#    Pense nos casos base (números menores ou iguais a 1).
#    Use um laço de repetição para testar os possíveis divisores do número.
numero_repeticoes = 0

for i in range (1, (entrada + 1)):
    if entrada % i == 0:
        numero_repeticoes += 1

if numero_repeticoes == 2:
    print(f'{entrada} é um número primo')
else:
    print(f'{entrada} não é um número primo')


# 3. Imprima o resultado final, seguindo exatamente o formato da Saída especificada.


# --- Fim do seu código ---