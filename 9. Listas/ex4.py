# -*- coding: utf-8 -*-

"""
**Listas - Exercício 4: Inversor de Palavras**

**Objetivo:**
Escrever um programa que recebe uma frase do usuário, a separa em palavras, inverte a ordem das palavras e imprime a frase invertida.

**Regras:**
1. Peça ao usuário para digitar uma frase. A resposta do `input()` será uma string única.
2. Use o método de string `.split()` para quebrar a frase em uma lista de palavras. O `split()` por padrão já separa as palavras pelos espaços.
3. Crie uma segunda lista, vazia, que se chamará `frase_invertida`.
4. Use um laço `for` para percorrer a sua lista de palavras original.
5. Dentro do laço, a cada palavra, use o método `.insert(0, palavra)` na sua **segunda lista** (`frase_invertida`). O método `.insert(0, ...)` sempre adiciona o novo item no **início** da lista. Pense no efeito que isso causa.
6. **Após o laço terminar**, a sua segunda lista conterá as palavras na ordem invertida.
7. O último passo é juntar as palavras da lista `frase_invertida` de volta em uma única string, separadas por espaços. A forma mais profissional de fazer isso é com o método de string `' '.join(sua_lista)`.
8. Imprima a frase final invertida.

**Entrada:**
- Uma string contendo uma frase.

**Saída:**
- A frase com a ordem das palavras invertida.

**Exemplo de Execução:**

Digite uma frase: eu amo programar em python
--------------------
Frase invertida: python em programar amo eu

**Tópicos Praticados:**
- Manipulação de Strings (`.split()`, `' '.join()`)
- Criação e manipulação de Listas
- Adição de itens no início com `.insert(0, item)`
- Laço `for` para iterar sobre uma lista
"""

# --- Início do seu código ---
frase = input('Digite uma frase: ')
frase_quebrada = frase.split()
print(frase_quebrada)


frase_invertida = []

for palavra in frase_quebrada:
    print(palavra, end=' ')
    frase_invertida.insert(0, palavra)
    
frase_final = ' '.join(frase_invertida)
print(f"Frase invertida: {frase_final}")
print(frase_final)


# --- Fim do seu código ---