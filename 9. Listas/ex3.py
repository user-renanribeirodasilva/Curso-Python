# -*- coding: utf-8 -*-

"""
**Listas - Exercício 3: Gerenciador de Tarefas Simples (To-Do List)**

**Objetivo:**
Criar um programa de linha de comando que permita ao usuário adicionar, listar e remover tarefas de uma lista. Este exercício introduz a remoção de itens e a estrutura de um menu interativo.

**Regras:**
1. Crie uma lista vazia no início para armazenar as tarefas (que serão strings).
2. Crie um laço infinito (`while True:`) que manterá o programa rodando. A única forma de sair será o usuário escolher a opção "Sair".
3. Dentro do laço, a cada repetição, mostre ao usuário um menu de opções:
   - "1: Adicionar Tarefa"
   - "2: Listar Tarefas"
   - "3: Remover Tarefa"
   - "4: Sair"
4. Peça ao usuário para digitar a opção desejada.
5. Use uma estrutura `if/elif/else` para tratar a escolha do usuário:
   - **Opção 1 (Adicionar):** Peça ao usuário para digitar a tarefa e use `.append()` para adicioná-la à lista.
   - **Opção 2 (Listar):** Verifique se a lista está vazia. Se estiver, imprima "Nenhuma tarefa na lista.". Se não, use um laço `for` para imprimir as tarefas de forma numerada (ex: "1. Comprar pão").
   - **Opção 3 (Remover):** Peça ao usuário o **número** da tarefa que ele quer remover. Converta esse número para um índice da lista (lembre-se que a lista começa no índice 0). Use o método `.pop(indice)` para remover a tarefa. (Ex: Se o usuário digitar 1, você deve remover o item no índice 0).
   - **Opção 4 (Sair):** Use o comando `break` para quebrar o laço `while` e encerrar o programa.
   - **Outra Opção:** Se o usuário digitar algo inválido, imprima "Opção inválida.".

**Exemplo de Execução:**
--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 1
Digite a nova tarefa: Comprar pão

--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 1
Digite a nova tarefa: Estudar Python

--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 2
--- Tarefas ---
1. Comprar pão
2. Estudar Python
---------------

--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 3
Qual o número da tarefa a ser removida? 1
Tarefa "Comprar pão" removida.

--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 2
--- Tarefas ---
1. Estudar Python
---------------

--- Menu de Tarefas ---
1: Adicionar Tarefa
2: Listar Tarefas
3: Remover Tarefa
4: Sair
Escolha uma opção: 4
Saindo do programa...

**Tópicos Praticados:**
- Listas (criação, `.append()`, `.pop()`)
- Laço `while True` com `break`
- `if/elif/else` para menus de opções
- Iteração sobre listas para exibição
- Conversão de tipos (`int()`)
- Manipulação de índices
"""

# --- Início do seu código ---
lista = []

while True:
    print('- "1: Adicionar Tarefa"\n- "2: Listar Tarefas"\n- "3: Remover Tarefa"\n- "4: Sair"')
    opcoes = input('Escolha uma das opções a cima: ')

    if opcoes == '1':
        tarefa = input('Digite o nome da tarefa a ser adicionada: ')
        lista.append(tarefa)
    elif opcoes == '2' and len(lista) == 0:
        print('Nenhuma tarefa na lista.')
    elif opcoes == '2':
        if len(lista) > 0:
            for i, valor in enumerate(lista, start = 1) :
                print(i, valor)
    elif opcoes == '3':
        remocao = int(input('Digite o número da tarefa que você deseja remover: '))
        indice = remocao - 1
        tarefa_removida = lista.pop(indice)
        print(f'A tarefa "{tarefa_removida}" foi removida com sucesso.')
    elif opcoes == '4':
        print('Encerrando...')
        break
    else:
        print('Opção inválida. Tente novamete: ')


# --- Fim do seu código ---