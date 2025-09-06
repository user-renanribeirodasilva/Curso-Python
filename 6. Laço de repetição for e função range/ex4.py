# Exercício 4 – Soma dos números de 1 a N
# Cenário: calcular a soma acumulada de uma sequência
# Regras:
# - Solicite ao usuário um número inteiro N
# - Use for com range para somar todos os números de 1 até N (inclusive)
# - Exiba o resultado final com f-string
# - Mostre também a mensagem "Cálculo encerrado"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

soma = 0

for i in range (1, (n + 1)):
    soma += i
    print(f'Soma até{i}: {soma}')
print(f'A soma total: {soma}')
print('Cálculo encerrado')