# Exercício 2 – Verificação de habilitação
# Cenário: sistema de transporte
# Regras:
# - O usuário deve informar sua idade
# - Se a idade for maior ou igual a 18, mostrar "Você pode tirar a habilitação"
# - Caso contrário, mostrar "Você ainda não pode tirar a habilitação"

# ESCREVA SEU CÓDIGO AQUI

idade = 17

if idade >= 18:
    print('Você pode tirar a habilitação')
else:
    print(f'Você ainda não pode tirar a habilitação, pois tem {idade} anos.')