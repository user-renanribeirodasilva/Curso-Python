# -*- coding: utf-8 -*-

"""
**Listas e Tuplas - Exercício 2: Gerenciamento de Usuários**

**Objetivo:**
Criar um sistema simples para gerenciar registros de usuários. Cada usuário será representado por uma tupla `(id, nome, email)`, e todos os usuários serão armazenados em uma lista.

**Regras:**
1.  Comece com uma lista pré-existente de usuários. A lista `usuarios` já deve conter algumas tuplas.
    - Exemplo: `usuarios = [(1, 'Renan', 'renan@email.com'), (2, 'Maria', 'maria@email.com')]`
2.  Crie um laço `for` para percorrer a lista `usuarios`.
3.  Dentro do laço, use o **desempacotamento de tuplas** para extrair o `id`, `nome` e `email` de cada usuário em variáveis separadas.
4.  Imprima os dados de cada usuário de forma organizada.
5.  **Adicionando um novo usuário:**
    a. Após o laço, simule a adição de um novo usuário. Peça ao usuário para digitar um `novo_nome` e um `novo_email`.
    b. O ID do novo usuário deve ser calculado automaticamente. Uma forma simples é pegar o ID do último usuário na lista e somar 1.
    c. Crie uma **nova tupla** `novo_usuario` com os dados coletados.
    d. Use o método `.append()` para adicionar essa `nova_tupla` à lista `usuarios`.
6.  Para finalizar, imprima a lista de usuários completa e atualizada.

**Entrada:**
- Nome e email para um novo usuário.

**Saída:**
- A lista de usuários iniciais.
- A lista de usuários atualizada após a adição.

**Exemplo de Execução:**

--- Lista de Usuários Inicial ---
ID: 1, Nome: Renan, Email: renan@email.com
ID: 2, Nome: Maria, Email: maria@email.com
---------------------------------

--- Adicionar Novo Usuário ---
Digite o nome do novo usuário: Carlos
Digite o email do novo usuário: carlos@email.com
---------------------------------

--- Lista de Usuários Atualizada ---
[(1, 'Renan', 'renan@email.com'), (2, 'Maria', 'maria@email.com'), (3, 'Carlos', 'carlos@email.com')]

**Tópicos Praticados:**
- Criação de uma Lista de Tuplas.
- Iteração sobre a lista e desempacotamento das tuplas.
- Acesso a elementos de listas e tuplas por índice.
- Adição de um novo item (tupla) a uma lista.
- Mutabilidade (a lista pode mudar) vs. Imutabilidade (a tupla não pode mudar).
"""

# --- Início do seu código ---
usuarios = [(1, 'Renan', 'renan@email.com'), (2, 'Maria', 'maria@email.com')]

for id_usuario, nome_usuario, email_usuario in usuarios:
    print(f'ID: {id_usuario}, Nome: {nome_usuario}, Email: {email_usuario}')
 
nome_usuario = input('Digite um novo nome:')
email_usuario = input('Digite um novo email: ')
novo_id = id_usuario + 1
 
novo_usuario = (novo_id, nome_usuario, email_usuario)
usuarios.append(novo_usuario)

print(f'Lista atualizada: {usuarios}')


# --- Fim do seu código ---