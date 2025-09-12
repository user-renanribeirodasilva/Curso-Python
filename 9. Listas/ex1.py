# -*- coding: utf-8 -*-

"""
**Listas - Exercício 1: Análise de Números**

**Objetivo:**
Escrever um programa que lê 5 números do usuário, armazena-os em uma lista e, ao final, exibe a soma, a média, o maior e o menor número da lista.

**Regras:**
1. Primeiro, crie uma lista vazia para armazenar os números.
2. Use um laço `for` que se repita 5 vezes para pedir os números.
3. A cada vez que o laço rodar, peça ao usuário para digitar um número e adicione este número à sua lista usando o método `.append()`.
4. **Após o primeiro laço terminar**, você terá uma lista com os 5 números. Agora, vamos analisá-la.
5. Crie as variáveis que você precisará para a análise: uma para a `soma` (iniciando em 0), uma para o `maior_numero` e uma para o `menor_numero`. (Dica: você pode inicializar o maior e o menor número com o primeiro item da lista).
6. Crie um **segundo laço `for`** para percorrer (iterar sobre) a sua lista de números.
7. Dentro deste segundo laço, a cada número:
   - Adicione o número à sua variável `soma`.
   - Use um `if` para verificar se o número atual é maior que o `maior_numero` que você tem guardado. Se for, atualize o `maior_numero`.
   - Use outro `if` para verificar se o número atual é menor que o `menor_numero`. Se for, atualize o `menor_numero`.
8. **Após o segundo laço terminar**, calcule a `media` (soma dividida pelo número de itens da lista). Para saber o número de itens, use a função `len()`.
9. Imprima os resultados de forma organizada.

**Entrada:**
- 5 números inteiros, um de cada vez.

**Saída:**
- A lista completa que foi digitada.
- A soma de todos os números.
- A média dos números.
- O maior número da lista.
- O menor número da lista.

**Exemplo de Execução:**
Digite o 1º número: 10
Digite o 2º número: 4
Digite o 3º número: 25
Digite o 4º número: 8
Digite o 5º número: 12

--------------------
Resultados:
Lista completa: [10, 4, 25, 8, 12]
Soma: 59
Média: 11.8
Maior número: 25
Menor número: 4

**Tópicos Praticados:**
- Criação de Listas `[]`
- Adição de itens a uma lista com `.append()`
- Laço `for` com `range` para obter dados
- Laço `for` para iterar sobre uma lista
- Uso da função `len()`
- Lógica com `if` para comparações
- Variáveis acumuladoras
"""

# --- Início do seu código ---
lista = []

for i in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)
print(f'Lista completa: {lista}')

soma = 0
maior_numero = lista[0]
menor_numero = lista[0]

for j in lista:
    soma += j
    if j > maior_numero:
        maior_numero = j
    if j < menor_numero:
        menor_numero = j

qts_itens = len(lista)
media = soma / qts_itens

print(f'A soma de todos os números: {soma}')
print(f'A média dos números: {media:.0f}')
print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')





# --- Fim do seu código ---