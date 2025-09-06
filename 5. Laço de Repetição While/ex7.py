# Exercício 7 – Verificação de número primo
# Cenário: verificar se um número fornecido pelo usuário é primo
# Regras:
# - Solicite ao usuário um número inteiro
# - Considere que um número primo é divisível apenas por 1 e por ele mesmo
# - Utilize while para testar todos os divisores possíveis do número
# - Se o número for primo, exiba "O número X é primo"
# - Caso contrário, exiba "O número X não é primo"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: ')) 

divisor = 1
contador = 0

while divisor <= n:
    if n % divisor == 0:
        contador += 1
    divisor += 1
    
if contador == 2:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é primo')