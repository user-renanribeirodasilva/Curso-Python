# Exercício 4 – Contagem regressiva
# Cenário: simulação de lançamento de foguete
# Regras:
# - Solicite ao usuário um número inteiro positivo
# - Faça a contagem regressiva desse número até 0
# - Exiba cada número da contagem em uma linha
# - Ao final, mostre a mensagem "Decolar!"

# ESCREVA SEU CÓDIGO AQUI

numero_usario = int(input('Digite um número: '))

# Primeira maneira
while True:
    print(numero_usario)
    numero_usario -= 1
    if numero_usario < 0:
        break
print('Decolar!')


# Segunda maneira
while numero_usario >= 0:
    print(numero_usario)
    numero_usario -= 1
print('Decolar!')