# Exercício 6 – Tabuada personalizada
# Cenário: gerar a tabuada de um número fornecido pelo usuário
# Regras:
# - Solicite ao usuário um número inteiro
# - Solicite ao usuário até que número deseja multiplicar (ex.: 1 a N)
# - Use while para gerar a tabuada do número até o limite fornecido
# - Exiba cada resultado no formato: "N x i = resultado"
# - Ao final, mostre a mensagem "Tabuada finalizada"

# ESCREVA SEU CÓDIGO AQUI

n1 = int(input('Digite um número inteiro: '))
n2 = int(input(f'Até que número você deseja múltiplicar o {n1} ? '))

contador = 0
    
while contador < n2:
    contador += 1
    resultado = contador * n1
    print(f'{n1} x {contador} = {resultado}')
print('Tabuada finalizada')
