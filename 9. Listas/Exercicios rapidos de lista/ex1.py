nomes = ['Renan', 'Fernanda', 'Francisco', 'Renata', 'Guilherme']

print(f'Primeiro nome: {nomes[0]}')
print(f'Último nome: {nomes[-1]}')

nomes.append('Marcelo')
print(nomes)

escolha_usuario = input('Escolha um nome que você que retirar: ')

if escolha_usuario in nomes:
    nomes.remove(escolha_usuario)
    print(f'O nome removido foi: {escolha_usuario}')
else:
    print(f'O nome {escolha_usuario} não esta na lista')
    
print(f'Lista completa: {nomes}')

