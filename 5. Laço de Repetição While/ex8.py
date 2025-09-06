# Multiplicação até atingir o limite
# Cenário: multiplicar um número por valores crescentes até que o resultado atinja ou ultrapasse um limite
# Regras:
# - Solicite ao usuário um número inteiro base
# - Solicite ao usuário o valor limite do resultado
# - Use while para multiplicar o número por 1, 2, 3... até o resultado atingir ou ultrapassar o limite
# - Exiba cada linha no formato: "N x i = resultado"
# - Ao final, mostre a mensagem "Tabuada finalizada"

# ESCREVA SEU CÓDIGO AQUI

base = int(input('Digite um número: '))
limite = int(input('Até que número você deseja multiplicar esse valor ? '))
contador = 1
resultado = base * contador

while resultado <= limite:
    print(f'{base} x {contador} = {resultado}')
    contador += 1
    resultado = base * contador
print('Fim!')
  