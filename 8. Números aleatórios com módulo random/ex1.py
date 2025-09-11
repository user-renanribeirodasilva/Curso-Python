# -*- coding: utf-8 -*-

"""
**Módulo Random - Exercício 1: Simulador de Lançamento de Moeda**

**Objetivo:**
Criar um programa que simula o lançamento de uma moeda várias vezes e conta quantas vezes o resultado foi "Cara" e quantas vezes foi "Coroa".

**Regras:**
1. O programa deve primeiro perguntar ao usuário quantas vezes a moeda deve ser lançada.
2. Use um laço `for` que se repita o número de vezes que o usuário especificou.
3. Dentro do laço, a cada "lançamento", o programa deve gerar um número aleatório para decidir o resultado:
   - Podemos combinar que o número 0 representa "Cara" e o número 1 representa "Coroa" (ou vice-versa). Use `random.randint(0, 1)`.
4. O programa deve ter duas variáveis de contagem: uma para as "Caras" e outra para as "Coroas". A cada lançamento, o contador apropriado deve ser incrementado.
5. Após o término de todos os lançamentos (o fim do laço), o programa deve imprimir o resultado final, mostrando o total de lançamentos, o número de "Caras" e o número de "Coroas".

**Entrada:**
- Um número inteiro, representando a quantidade de lançamentos.

**Saída:**
- Um resumo final com a contagem dos resultados.

**Exemplo de Execução:**

Quantas vezes você quer lançar a moeda? 1000
Lançando a moeda 1000 vezes...
--------------------
Resultado Final:
Caras: 492
Coroas: 508

**Tópicos Praticados:**
- `import random` e `random.randint`
- Laço de Repetição (`for` e `range`)
- Desvios Condicionais (`if/else`)
- Variáveis de contagem
- Entrada e Saída de dados (`input`, `print` com f-strings)
"""

# --- Início do seu código ---
import random

lancamento_moeda = int(input('Quantas vezes a moeda deve ser lançada? '))
contagem_cara = 0
contagem_coroa = 0

print(f'Lançando a moeda {lancamento_moeda} vezes...')

for i in range(lancamento_moeda):
    resultado = random.randint(0, 1)
    if resultado == 0:
        contagem_cara += 1
    else:
        contagem_coroa += 1
print(f'Resultado Final:\nCaras: {contagem_cara}\nCoroas: {contagem_coroa}')

# --- Fim do seu código ---



















