# Exercício 3 – Tabuada até 10
# Cenário: geração de tabuada para estudo
# Regras:
# - Solicite ao usuário um número inteiro
# - Exiba a tabuada desse número de 1 a 10 no formato: "N x i = resultado"
# - Ao final, mostre a mensagem "Tabuada finalizada"

# ESCREVA SEU CÓDIGO AQUI

numero_usuario = int(input('Digite um número: '))

contador = 1

while contador <= 10:
    resultado = numero_usuario * contador
    print(f"{numero_usuario} x {contador} = {resultado}")
    contador += 1
print('Tabuada finalizada')