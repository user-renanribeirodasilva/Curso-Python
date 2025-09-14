numeros = (1,2,3,4,5,6,7,8,9,10)

numero_usuario = int(input('Digite um número: '))

quantidade = numeros.count(numero_usuario)

print(f'O número {numero_usuario} aparece {quantidade} vezes na tupla')

posicoes = []
for i, valor in enumerate(numeros):
    if valor == numero_usuario:
        posicoes.append(i)
print(f'Na posição: {posicoes}')
