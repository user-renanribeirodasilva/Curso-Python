# Exercício 6 – Tabuada personalizada com limite
# Cenário: gerar a tabuada de um número fornecido pelo usuário até um limite definido
# Regras:
# - Solicite ao usuário um número inteiro
# - Solicite ao usuário até que número deseja multiplicar (ex.: 1 a N)
# - Use for para gerar a tabuada do número até o limite fornecido
# - Exiba cada resultado no formato: "N x i = resultado"
# - Ao final, mostre a mensagem "Tabuada finalizada"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))
n2 = int(input('Até que número deseja múltiplicar ? : '))

for i in range (1, (n2 + 1)):
    print(f'{n} x {i} = {n * i}')