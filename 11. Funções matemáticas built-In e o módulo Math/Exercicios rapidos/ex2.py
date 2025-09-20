import math 

numero_inteiro = int(input('Digite um número inteiro: '))

numero_fatoril = math.factorial(numero_inteiro)
print(f'O fatorial do número {numero_inteiro} é {numero_fatoril}')

numero_decimal = float(input('Digite um número decimal: '))

arredondar_cima = math.ceil(numero_decimal)
arredondar_baixo = math.floor(numero_decimal)
print(f'O número {numero_decimal} arredondado para cima é {arredondar_cima} e arredondado para baixo é {arredondar_baixo}')