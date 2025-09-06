# Exercício 2 – Comparações com Strings
# 1. Crie duas variáveis com nomes de pessoas, por exemplo: nome1 e nome2
# 2. Verifique se os nomes são iguais
# 3. Verifique se o nome1 vem antes do nome2 em ordem alfabética
# 4. Mostre cada resultado em frases usando f-strings

# ESCREVA SEU CÓDIGO AQUI

nome1 = 'Renan'
nome2 = 'Guilherme'

verifica_nomes = nome1 == nome2
print(verifica_nomes)

compara = nome1 < nome2
print(compara)

print(f'O nome {nome1} é igual ao nome {nome2}: {verifica_nomes}. O nome {nome1} vem antes do nome {nome2}: {compara}')