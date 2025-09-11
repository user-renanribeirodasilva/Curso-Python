"""
**Módulo Random - Exercício 2: Simulador de Lançamento de Dado**

**Objetivo:**
Criar um programa que simula o lançamento de um dado de seis lados (D6) várias vezes e mostra a frequência de cada resultado.

**Regras:**
1. O programa deve perguntar ao usuário quantas vezes o dado deve ser lançado.
2. Use um laço `for` para simular cada lançamento.
3. A cada lançamento, gere um número inteiro aleatório entre 1 e 6 (inclusive) para representar a face do dado que caiu para cima.
4. Você precisará de seis variáveis de contagem, uma para cada face do dado (face_1, face_2, etc.).
5. Dentro do laço, use uma estrutura `if/elif/else` para verificar o resultado do lançamento e incrementar o contador correto.
6. Ao final de todos os lançamentos, imprima um relatório mostrando quantas vezes cada número apareceu.

**Entrada:**
- Um número inteiro, representando a quantidade de lançamentos.

**Saída:**
- Um resumo final com a contagem para cada face do dado.

**Exemplo de Execução:**

Quantas vezes você quer lançar o dado? 10000
Lançando o dado 10000 vezes...
--------------------
Resultado Final:
Face 1: 1655 vezes
Face 2: 1680 vezes
Face 3: 1644 vezes
Face 4: 1671 vezes
Face 5: 1668 vezes
Face 6: 1682 vezes

**Tópicos Praticados:**
- `import random` e `random.randint`
- Laço `for`
- Estrutura `if/elif/else` completa
- Múltiplas variáveis de contagem
- Entrada e Saída de dados
"""

# --- Início do seu código ---
import random

contagem = 0
face1 = 0  
face2 = 0  
face3 = 0  
face4 = 0  
face5 = 0  
face6 = 0 

n = int(input('Quantas vezes você quer lançar o dado? '))

print(f'Lançando o dado {n} vezes...')

for i in range(n):
    lancamento_dado = random.randint(1, 6)
    contagem += 1

    if lancamento_dado == 1:
        face1 += 1
    elif lancamento_dado == 2:
        face2 += 1
    elif lancamento_dado == 3:
        face3 += 1
    elif lancamento_dado == 4:
        face4 += 1
    elif lancamento_dado == 5:
        face5 += 1
    else:
        face6 += 1

print('--------------------')

print(f'Resultado Final:\nFace 1: {face1} vezes\nFace 2: {face2} vezes\nFace 3: {face3} vezes\nFace 4: {face4} vezes\nFace 5: {face5} vezes\nFace 6: {face6} vezes\nTotal de vezes: {contagem}')
# --- Fim do seu código ---