"""
**Exercício 1 (Reforço): Quadrado Vazado**

**Objetivo:**
Escrever um programa que solicita ao usuário um número `N` e desenha a "borda" de um quadrado de tamanho N x N.

**Entrada:**
- Um número inteiro positivo `N` fornecido pelo usuário.

**Saída:**
- Um padrão de asteriscos que forma um quadrado vazado.

**Exemplo:**
- Entrada: 5
  Saída:
  *****
  * *
  * *
  * *
  *****

- Entrada: 4
  Saída:
  ****
  * *
  * *
  ****

**Tópicos Praticados:**
- Laços Encadeados
- Lógica condicional (if/else) dentro de laços
"""

# --- Início do seu código ---

# Dicas para pensar:
# 1. A estrutura externa é um quadrado. Isso significa que tanto o laço de fora (linhas) quanto o de dentro (colunas) devem rodar N vezes. Uma boa forma é usar `range(n)`.
#
# 2. A "mágica" acontece DENTRO do laço interno. Para cada posição (cada célula da grade), você precisa tomar uma DECISÃO:
#    - Devo imprimir um asterisco `*`?
#    - Ou devo imprimir um espaço em branco ` `?
#
# 3. Quando devemos imprimir um asterisco? Apenas se estivermos na borda. E o que é a "borda"?
#    - É a primeira linha (linha 0)
#    - OU a última linha (linha N-1)
#    - OU a primeira coluna (coluna 0)
#    - OU a última coluna (coluna N-1)
#
# 4. Use as variáveis `i` (para a linha atual) e `j` (para a coluna atual) para verificar essas condições com um `if/else`.

n = int(input('Digite o tamanho do quadrado: '))

# Laço para as linhas (de 0 a n-1)
for i in range(n):

    # Laço para as colunas (de 0 a n-1)
    for j in range(n):

        # AQUI DENTRO vai a sua lógica if/else para decidir
        # se imprime '*' ou ' '
        
        ...

    # Não se esqueça de pular a linha no final de cada rodada do laço de fora
    print()

# --- Fim do seu código ---