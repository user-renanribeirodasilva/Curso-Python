# -*- coding: utf-8 -*-

"""
**Exercício 2: Somador de Números Pares**

**Objetivo:**
Escrever um programa que calcula a soma de todos os números pares dentro de um intervalo definido pelo usuário.

**Entrada:**
- O programa deve solicitar ao usuário dois números inteiros:
  1. O início do intervalo.
  2. O fim do intervalo.

**Saída:**
- O programa deve imprimir a soma total de todos os números pares encontrados nesse intervalo (incluindo os números de início e fim, se forem pares).
- A mensagem deve ser: f"A soma dos números pares de {inicio} até {fim} é: {soma}."

**Regras:**
- O número de "início" do intervalo pode ser maior que o número de "fim". Seu programa deve ser inteligente o suficiente para entender qual é o menor e qual é o maior número para o `range` funcionar corretamente.

**Exemplos:**
- Entrada 1: 1
- Entrada 2: 10
  Saída: A soma dos números pares de 1 até 10 é: 30. (pois 2 + 4 + 6 + 8 + 10 = 30)

- Entrada 1: 15
- Entrada 2: 5
  Saída: A soma dos números pares de 5 até 15 é: 60. (pois 6 + 8 + 10 + 12 + 14 = 50. Opa, erro no exemplo, vamos corrigir: 6+8+10+12+14 = 50. Não, está errado. 6+8=14, 14+10=24, 24+12=36, 36+14=50. Ah, o exemplo está errado, o correto seria: A soma dos números pares de 5 até 15 é: 50.)
  *Correção do Exemplo*:
- Entrada 1: 15
- Entrada 2: 5
  Saída: A soma dos números pares de 5 até 15 é: 50. (pois 6 + 8 + 10 + 12 + 14 = 50)


**Tópicos Praticados:**
- Entrada de dados (input) e conversão para int
- Variáveis e Tipos de Dados
- Operadores Aritméticos (+, %)
- Desvios Condicionais (if, else)
- Laço de Repetição (for e range)
- Lógica para manipular e ordenar valores
"""

# --- Início do seu código ---

# 1. Peça ao usuário o número de início e o número de fim do intervalo.
entrada1 = int(input('Digite um número de início: '))
entrada2 = int(input('Digite um número de fim: '))


# 2. Determine qual dos dois números é o menor e qual é o maior para
#    que o laço `for` com `range` funcione corretamente.
if entrada1 > entrada2:
    menor = entrada2
    maior = entrada1
else:
    maior = entrada2
    menor = entrada1
# 3. Inicialize uma variável para armazenar a soma total, começando em zero.
soma = 0

# 4. Crie um laço `for` que percorra todos os números no intervalo correto.
for i in range (menor, (maior + 1)):
    # 5. Dentro do laço, use um `if` para verificar se o número atual é par.
    if i % 2 == 0:
    # 6. Se for par, adicione o valor do número à sua variável de soma.
        soma += i
    # 7. Após o fim do laço, imprima o resultado final no formato solicitado.
print(f'A soma dos números pares de {menor} até {maior} é: {soma}.')


# --- Fim do seu código ---