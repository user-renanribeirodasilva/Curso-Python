# Exercício 3 – Tabuada até 10
# Cenário: gerar a tabuada de um número fornecido pelo usuário
# Regras:
# - Solicite ao usuário um número inteiro
# - Exiba a tabuada desse número de 1 a 10 no formato: "N x i = resultado"
# - Use for com range para gerar os multiplicadores
# - Ao final, mostre a mensagem "Tabuada finalizada"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

for i in range (1, 11):
    print(f'{n} x {i} = {n * i}')
print('Tabuada finalizada')
