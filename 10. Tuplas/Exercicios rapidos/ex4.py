cores = ('azul', 'amarelo', 'vermelho', 'laranja', 'preto')

usuario = input('Digite um cor: ')

if usuario in cores:
    print(f'A cor {usuario} está na lista')
else:
    print(f'A cor {usuario} não está na lista')