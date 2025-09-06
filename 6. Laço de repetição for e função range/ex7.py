# Exercício 7 – Verificação de número primo
# Cenário: verificar se um número fornecido pelo usuário é primo
# Regras:
# - Solicite ao usuário um número inteiro
# - Considere que um número primo é divisível apenas por 1 e por ele mesmo
# - Use for junto com range para testar todos os divisores possíveis do número
# - Se o número for primo, exiba "O número X é primo"
# - Caso contrário, exiba "O número X não é primo"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

quantidade = 0

for i in range (1, (n+1)):
    if n % i == 0:
        quantidade += 1

if quantidade == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')