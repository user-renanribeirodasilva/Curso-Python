import math

calculo = input('Digite C para área do Círculo ou Q para área do Quadrado: ').lower()

if calculo == 'c':
    raio_circulo = int(input('Digite o raio do círculo: '))
    area_circulo = math.pi * (raio_circulo ** 2)
    print(f'A área do círculo é {area_circulo:.2f}')
elif calculo == 'q':
    lado_quadrado = int(input('Digite o lado do quadrado: '))
    area_quadrado = math.pow(lado_quadrado, 2)
    print(f'A área do quadrado é {int(area_quadrado)}')
else:
    print(f'Opção {calculo} inválida.')
    


