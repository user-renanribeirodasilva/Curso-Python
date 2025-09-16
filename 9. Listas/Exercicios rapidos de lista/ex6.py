tarefas = ["Estudar Python", "Lavar a louça", "Passear com o cachorro"]

tarefa_concluida = input('Digite o nome de uma tarefa que você concluiu: ')

if tarefa_concluida in tarefas:
    tarefas.remove(tarefa_concluida)
else:
    print(f'{tarefa_concluida} não está na lista!')
    
print(f'Lista atualizada: {tarefas}')