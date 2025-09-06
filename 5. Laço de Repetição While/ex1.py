# Exercício 1 – Contador até um número
# Cenário: criar um contador que exibe números de 1 até o número informado pelo usuário
# Regras:
# - Solicite ao usuário um número inteiro positivo
# - Use um laço while para contar de 1 até o número informado
# - Exiba cada número usando f-strings
# - No final, exiba uma mensagem de conclusão indicando o último número contado

# ESCREVA SEU CÓDIGO AQUI

numero_usuario = int(input('Digite um número: '))

contagem = 1

while contagem <= numero_usuario:
    print(f'Número atual: {contagem}')
    contagem += 1
print(f'Contagem finalizada! Último número contado: {numero_usuario}')