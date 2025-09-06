# Exercício 5 – Contagem regressiva
# Cenário: exibir uma contagem regressiva até chegar a zero
# Regras:
# - Solicite ao usuário um número inteiro N
# - Use for junto com range para contar de N até 0
# - Cada número deve aparecer em uma nova linha
# - Ao final, mostre a mensagem "Fim da contagem regressiva"

# ESCREVA SEU CÓDIGO AQUI

n = int(input('Digite um número: '))

for i in range (n, -1, -1):
    print(i)
print("Fim da contagem regressiva")