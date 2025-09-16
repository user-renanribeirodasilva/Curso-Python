numeros = [1,2,3,4,5,6,7,8,9,10]

numero_pares = []
numero_impares = []

maior_numero = max(numeros)
menor_numero = min(numeros)

for numero in numeros:
    if numero % 2 == 0:
        numero_pares.append(numero)
print(f'Os números pares são:{numero_pares}')

for numero in numeros:
    if numero % 2 != 0:
        numero_impares.append(numero)
print(f'Os números ímpares são:{numero_impares}')

print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')

soma_total = sum(numeros)
print(f'A soma total é: {soma_total}')
