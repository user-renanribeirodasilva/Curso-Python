# Exercício 5 – Soma de números positivos
# Cenário: acumulador de valores informados pelo usuário
# Regras:
# - Solicite ao usuário que digite números inteiros positivos
# - Enquanto o usuário digitar um número positivo, acumule a soma
# - Se o usuário digitar um número negativo, finalize o programa
# - Exiba a soma total dos números positivos digitados

# ESCREVA SEU CÓDIGO AQUI

soma = 0

# maneira 1:
n = int(input('Digite um numero '))

while n >= 0:
    soma += n
    n = int(input('Digite um numero '))
print(f'Soma total: {soma}')

# maneira 2:
while True:
    n = int(input('Digite um numero '))
    if n < 0:
        break
    soma += n
print(f'Soma total: {soma}')
