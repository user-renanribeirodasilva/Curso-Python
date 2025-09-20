import math 

a = int(input('Digite o valor do cateto a: '))
b = int(input('Digite o valor do cateto b: '))

soma_quadradoA = math.pow(a,2)
soma_quadradoB = math.pow(b,2)

resultado = (soma_quadradoA + soma_quadradoB) 

hipotenusa = math.sqrt(resultado)

print(f'A hipotenusa do triângulo é {hipotenusa:.2f}')