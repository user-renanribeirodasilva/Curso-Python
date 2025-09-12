# -*- coding: utf-8 -*-

"""
**Simulação: Corrida de Caracóis**

**Objetivo:**
Criar uma simulação de corrida entre dois caracóis. O objetivo é usar um laço `while` para controlar a corrida, o `random.randint` para simular o movimento de cada caracol a cada rodada, e `if` para determinar o vencedor. Este exercício mistura tudo que aprendemos.

**Regras:**
1. Defina uma variável para a distância total da corrida. Por exemplo, `DISTANCIA_CORRIDA = 20`.
2. Crie e inicialize variáveis para a posição de dois competidores, o "Caracol A" e o "Caracol B". Ambos começam na posição 0.
3. Crie uma variável para contar as rodadas da corrida, começando em 1.
4. Use um laço `while` que continue executando a corrida enquanto NENHUM dos caracóis tiver alcançado ou ultrapassado a `DISTANCIA_CORRIDA`.
5. Dentro do laço, a cada "rodada":
   - Imprima o número da rodada atual.
   - Sorteie um avanço para o Caracol A (um número aleatório entre 1 e 3).
   - Sorteie um avanço para o Caracol B (também entre 1 e 3).
   - Atualize a posição de cada caracol somando o avanço sorteado.
   - Imprima o status da rodada, mostrando a posição atual de cada caracol.
   - Incremente o contador de rodadas.
6. Após o laço terminar (o que significa que pelo menos um caracol cruzou a linha de chegada), use uma estrutura `if/elif/else` para verificar e anunciar o resultado:
   - Se o Caracol A chegou e o B não, A venceu.
   - Se o Caracol B chegou e o A não, B venceu.
   - Se ambos cruzaram a linha de chegada na mesma rodada, anuncie um empate.

**Entrada:**
- Nenhuma entrada do usuário é necessária. Os valores são definidos no código.

**Saída:**
- O status de cada rodada da corrida.
- Uma mensagem final anunciando o vencedor ou se houve um empate.

**Exemplo de Execução (os valores serão diferentes a cada vez):**

--- Início da Corrida! ---
Rodada 1:
Caracol A avançou 2 passos e está na posição 2.
Caracol B avançou 3 passos e está na posição 3.
--------------------
Rodada 2:
Caracol A avançou 1 passo e está na posição 3.
Caracol B avançou 2 passos e está na posição 5.
--------------------
... (várias rodadas depois) ...
--------------------
Rodada 9:
Caracol A avançou 3 passos e está na posição 19.
Caracol B avançou 2 passos e está na posição 21.
--------------------
Fim da corrida!
O Caracol B venceu a corrida em 9 rodadas!

**Tópicos Praticados:**
- `random.randint`
- Laço `while`
- Variáveis (contadores e acumuladores de posição)
- Operadores Aritméticos, de Comparação e Lógicos (`and`)
- `if/elif/else`
- `print` com f-strings
"""

# --- Início do seu código ---
import random

distancia_total = 100

posicao_caracolA = 0
posicao_caracolB = 0

rodadas_corridas = 0

while posicao_caracolA < distancia_total and posicao_caracolB < distancia_total:
    rodadas_corridas += 1
    sorteioA = random.randint(1, 3)
    posicao_caracolA += sorteioA
    sorteioB = random.randint(1, 3)
    posicao_caracolB += sorteioB
    print(f'Posição atual Caracol A: {posicao_caracolA}')
    print(f'Posição atual Caracol B: {posicao_caracolB}')
if posicao_caracolA >= distancia_total and posicao_caracolB >= distancia_total:
    print(f'Houve empate entre o Caracol A e o Caracol B: {rodadas_corridas} rodadas!')
elif posicao_caracolA >= distancia_total:
    print(f'O Caracol A venceu a corrida em {rodadas_corridas} rodadas!')
elif posicao_caracolB >= distancia_total:
    print(f'O Caracol B venceu a corrida em {rodadas_corridas} rodadas!')

# --- Fim do seu código ---