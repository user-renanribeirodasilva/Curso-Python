# Exercício 8 – Conversão de Temperatura
# 1. Crie uma variável 'celsius' com uma temperatura em Celsius
# 2. Converta para Fahrenheit usando a fórmula: F = C * 9/5 + 32
# 3. Mostre a frase: "20°C equivalem a 68.0°F", formatando com 1 casa decimal

# ESCREVA SEU CÓDIGO AQUI

celsius = 32

fahrenheit = (celsius * 9/5) + 32
print(f'{celsius}°C equivalem a {fahrenheit:.1f}°F')