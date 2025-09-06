# Exercício 2 – Mini-desafio de operadores lógicos
# Cenário: validação de acesso a um sistema
# Regras:
# - A pessoa só pode acessar se for maior de idade (idade >= 18) 
#   E tiver status de assinatura ativo (assinatura = True)
# - Se a pessoa não atender a algum critério, deve mostrar que o acesso é negado

# 1. Crie variáveis: idade, assinatura (True/False)
# 2. Use operadores lógicos para verificar se a pessoa pode acessar
# 3. Mostre o resultado usando f-strings

# ESCREVA SEU CÓDIGO AQUI
idade = 18
assinatura = True

verificacao = idade >= 18 and assinatura 

print(f'Seu status é: {verificacao}')

