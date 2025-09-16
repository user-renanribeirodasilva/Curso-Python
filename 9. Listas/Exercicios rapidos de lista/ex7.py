numeros = [10, 23, 4, 7, 15, 9, 22, 8]

for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        print(f'Número par {numero} encontrado na posição {indice}')
    