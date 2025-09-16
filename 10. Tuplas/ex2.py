# -*- coding: utf-8 -*-

"""
**Tuplas - Exercício 1: Trabalhando com Coordenadas**

**Objetivo:**
Praticar a criação de tuplas, o acesso a seus elementos por índice e a técnica de "desempacotamento" (unpacking) para atribuir os valores da tupla a variáveis individuais.

**Regras:**
1. Crie uma tupla chamada `ponto` para representar uma coordenada (x, y) no plano cartesiano. Atribua a ela os valores `(10, 20)`.
2. Acesse e imprima o valor da coordenada X (o primeiro item) usando seu índice.
3. Acesse e imprima o valor da coordenada Y (o segundo item) usando seu índice.
4. **Desempacotamento:** Em uma única linha, crie duas novas variáveis, `x` e `y`, e atribua a elas os valores da tupla `ponto`. (A sintaxe para isso é `x, y = ponto`).
5. Imprima os valores das novas variáveis `x` e `y` para confirmar que o desempacotamento funcionou.
6. **Teste de Imutabilidade (Opcional, mas importante):** Abaixo do seu código, descomente (apague o `#`) da linha `# ponto[0] = 30` e tente rodar o programa. Observe o `TypeError` que o Python gera. Isso vai provar que você não pode alterar uma tupla depois de criada. Lembre-se de comentar a linha de volta para o código funcionar.

**Entrada:**
- Nenhuma entrada do usuário é necessária.

**Saída:**
- Os valores das coordenadas acessados de diferentes maneiras.

**Exemplo de Saída Esperada:**

Acessando por índice:
Coordenada X: 10
Coordenada Y: 20

Acessando por desempacotamento:
Valor de x: 10
Valor de y: 20

**Tópicos Praticados:**
- Criação de Tuplas `()`
- Acesso a elementos por Índice `[ ]`
- Desempacotamento (Unpacking)
- Imutabilidade (a principal característica das Tuplas)
"""

# --- Início do seu código ---
ponto = (10, 20)

print(f'Primero valor:' + str((ponto)[0]))
print(f'Segundo valor: '+ str((ponto)[1]))

x, y = ponto

print(f'Cordenada X: {x}\nCordenada Y: {y}')

# ponto[0] = 11
# print(type(ponto))

# --- Fim do seu código ---

# --- Teste de Imutabilidade (Descomente a linha abaixo para ver o erro) ---
# ponto[0] = 30