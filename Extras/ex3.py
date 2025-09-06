# -*- coding: utf-8 -*-

"""
**Exercício 3: Contador de Múltiplos**

**Objetivo:**
Escrever um programa que conta quantos números múltiplos de um valor específico existem dentro de um intervalo definido pelo usuário.

**Entrada:**
- O programa deve solicitar ao usuário três números inteiros:
  1. O início do intervalo.
  2. O fim do intervalo.
  3. O número para verificar se é múltiplo (o "divisor").

**Saída:**
- O programa deve imprimir a contagem total de múltiplos encontrados.
- A mensagem deve ser: f"Existem {contagem} múltiplos de {divisor} entre {inicio} e {fim}."

**Regras:**
- O número de "início" do intervalo pode ser maior que o de "fim". Seu programa deve, novamente, ser inteligente para ordenar o intervalo corretamente.
- Um número `A` é múltiplo de `B` se o resto da divisão de `A` por `B` for zero (`A % B == 0`).

**Exemplos:**
- Entrada 1 (inicio): 1
- Entrada 2 (fim): 20
- Entrada 3 (divisor): 3
  Saída: Existem 6 múltiplos de 3 entre 1 e 20. (Os múltiplos são: 3, 6, 9, 12, 15, 18)

- Entrada 1 (inicio): 50
- Entrada 2 (fim): 10
- Entrada 3 (divisor): 7
  Saída: Existem 6 múltiplos de 7 entre 10 e 50. (Os múltiplos são: 14, 21, 28, 35, 42, 49)

**Tópicos Praticados:**
- Lógica para manipular e ordenar valores (if/else)
- Laço de Repetição (for e range)
- Operadores Aritméticos (%) e de Comparação (==)
- Variáveis de contagem
- Entrada/Saída de dados
"""

# --- Início do seu código ---

# 1. Peça ao usuário o início, o fim e o divisor.
n_inicio = int(input('Digite o número inícial: '))
n_final = int(input('Digite o número final: '))
divisor = int(input('Digite o número divisor: '))


# 2. Use a mesma lógica `if/else` do exercício anterior para
#    definir as variáveis `menor` e `maior`.
if n_inicio > n_final:
    menor = n_final
    maior = n_inicio
else:
    maior = n_final
    menor = n_inicio

# 3. Inicialize uma variável para a contagem, começando em zero.
soma = 0
multiplos = ''
# 4. Crie um laço `for` que percorra todos os números no intervalo (de `menor` até `maior`).
for i in range (menor, (maior + 1)):
    if i % divisor == 0:
        soma += 1
        multiplos += str(i) + ', '
print(f'Existem {soma} múltiplos de {divisor} entre {menor} e {maior}.')
if soma > 0:
    print(f'Os múltiplos são: {multiplos}')

  # Saída: Existem 6 múltiplos de 7 entre 10 e 50. (Os múltiplos são: 14, 21, 28, 35, 42, 49)



# 5. Dentro do laço, verifique se o número atual é múltiplo do divisor.


# 6. Se for um múltiplo, incremente sua variável de contagem.


# 7. Após o laço terminar, imprima o resultado final no formato solicitado.


# --- Fim do seu código ---