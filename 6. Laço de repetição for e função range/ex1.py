# Exercício 1 – Números de 1 a N
# Cenário: exibir todos os números de 1 até um número fornecido pelo usuário
# Regras:
# - Solicite ao usuário um número inteiro N
# - Use for junto com range para exibir todos os números de 1 até N (inclusive)
# - Cada número deve aparecer em uma nova linha
# - Ao final, mostre a mensagem "Fim da contagem"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

for i in range (1, (n + 1)):
    print(i)
print('Fim contagem')