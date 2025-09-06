# Exercício 2 – Números pares de 1 a N
# Cenário: exibir apenas os números pares em uma sequência
# Regras:
# - Solicite ao usuário um número inteiro N
# - Use for com range para percorrer de 1 até N (inclusive)
# - Exiba apenas os números pares
# - Cada número deve aparecer em uma nova linha
# - Ao final, mostre a mensagem "Fim da listagem de pares"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

for i in range (1, (n + 1)):
    if i % 2 == 0:
        print(i)
print('Fim da listagem de pares')