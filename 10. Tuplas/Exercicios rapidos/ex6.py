numeros = (1,2,3,4,5,6, 6,7,8,8)
print(numeros)

numeros_unicos = set(numeros)
quantidade_diferentes = len(numeros_unicos)
print(f'A quantidade de números únicos é: {quantidade_diferentes}')

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f'O maior valor é: {maior_numero}')
print(f'O menor valor é: {menor_numero}')

soma_total = sum(numeros)
print(f'A soma total é: {soma_total}')

media = soma_total / len(numeros)
print(f'A média é: {media}')