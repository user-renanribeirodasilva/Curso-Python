# Exercício 2 – Soma até o usuário decidir parar
# Cenário: criar um programa que soma números enquanto o usuário quiser
# Regras:
# - Solicite números inteiros ao usuário repetidamente
# - Some todos os números informados
# - Pergunte ao usuário após cada entrada se ele quer continuar (s/n)
# - Use um laço while para controlar a repetição
# - Exiba a soma acumulada a cada entrada usando f-strings
# - Ao final, mostre a soma total de todos os números informados

# ESCREVA SEU CÓDIGO AQUI
numero_usuario = int(input('Digite um número: '))

continuar = input('Você deseja continuar? s/n ').lower()

soma = 0

while continuar == 's':
    soma += numero_usuario
    print(f'O valor acumulado é: {soma}')
    numero_usuario = int(input('Digite um número: '))
    continuar = input('Você deseja continuar? s/n ').lower()
print(f'A soma total acumulada é: {soma}')