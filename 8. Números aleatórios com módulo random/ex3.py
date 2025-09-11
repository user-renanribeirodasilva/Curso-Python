# -*- coding: utf-8 -*-

"""
**Sorteador de Números da Mega-Sena**

**Objetivo:**
Criar um programa simples que simula um sorteio da Mega-Sena, gerando os 6 números aleatórios.

**Regras:**
1. O programa não precisa de input do usuário.
2. Ele deve sortear 6 números inteiros.
3. Cada número deve estar no intervalo de 1 a 60 (inclusive).
4. O programa deve imprimir os 6 números sorteados.
5. **Observação Importante:** Para este exercício, **os números podem se repetir**. O foco aqui é apenas na geração aleatória dentro de um laço.

**Entrada:**
- Nenhuma.

**Saída:**
- Os 6 números sorteados.

**Exemplo de Execução:**

Sorteando os 6 números da Mega-Sena...
--------------------
Os números sorteados foram: 7 15 22 31 45 58

**Tópicos Praticados:**
- `import random` e `random.randint`
- Laço `for` com `range` fixo
- Saída de dados com `print` e o parâmetro `end`
"""

# --- Início do seu código ---
import random

print(f'Os números sorteados foram: ')

for i in range (6):
    sorteio = random.randint(1, 60)

    print(sorteio, end=' ')




# --- Fim do seu código ---