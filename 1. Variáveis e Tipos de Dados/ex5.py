# Exercício 5 – Calculadora de IMC
# 1. Crie variáveis para:
#    - peso (em kg, float)
#    - altura (em metros, float)
# 2. Calcule o IMC: IMC = peso / (altura ** 2)
# 3. Mostre a frase: "Uma pessoa com 1.73m de altura e 70kg tem IMC de 23.39"
#    Formate o IMC com 2 casas decimais

# ESCREVA SEU CÓDIGO AQUI

peso = 67.8
altura = 1.73

imc = peso / (altura**2)
print(f'Uma pessoa com {altura} de altura e {peso}kg tem IMC de {imc:.2f}')