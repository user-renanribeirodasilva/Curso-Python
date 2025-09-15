numeros = (19, 21, 22, 22, 25, 53, 55, 33, 28, 48)

print(numeros)

# mostrar os 3 primeiros:
tres_primeiros = numeros[:3]
print(tres_primeiros)

#mostrar os 3 ultimos
tres_ultimos = numeros[-3:]
print(tres_ultimos)

menor = min(numeros)
print(menor)
maior = max(numeros)
print(maior)

soma_total = sum(numeros)
print(soma_total)

media = soma_total / len(numeros)
print(media)

contagem = numeros.count(5)
print(contagem)

numero_usuario = int(input('Digite um número: '))

posicoes = []
for indice, valor in enumerate(numeros):
    if numero_usuario == valor:
        posicoes.append(indice)
        
if posicoes:
    print(f'O número {numero_usuario} aparece em posições: {posicoes}')
else:
    print(f'O número {numero_usuario} não aparece na tupla')