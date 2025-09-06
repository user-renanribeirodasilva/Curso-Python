# Exercício 1 – Operadores Lógicos
# 1. Crie duas variáveis, idade e renda
# 2. Verifique se a pessoa é maior de idade (>=18) E tem renda maior que 2000
# 3. Verifique se a pessoa é menor de idade OU tem renda menor ou igual a 2000
# 4. Inverta o resultado da primeira verificação usando NOT
# 5. Mostre cada resultado em frases usando f-strings

# Dica: use and, or, not

# ESCREVA SEU CÓDIGO AQUI

idade = 25
renda = 1000

verificacao1 = idade >= 18 and renda > 2000
verificacao2 = idade < 18 or renda <= 2000
print(f'A pessoa é maior de idade e tem renda maior que 2000 ? {verificacao1}')
print(f'A pessoa é menor de idade ou tem renda menor que 2000 ? {verificacao2}')
print(f'O inverso da verificação 2 é: {not verificacao2}')

