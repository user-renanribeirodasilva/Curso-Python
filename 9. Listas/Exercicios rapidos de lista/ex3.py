nomes = ['Ana', 'Alice', 'Davi', 'Samira', 'Vitor', 'Bernardo']

for nome in nomes:
    if len(nome) > 5:
        print(nome)

for nome in nomes:
    print(f'O nome {nome} tem {len(nome)} letras')
    
    
usuario = input('Digite um nome: ')

if usuario in nomes:
    print(f'O nome {usuario} está na lista')
else:
    print(f'O nome {usuario} não está na lista')
        
