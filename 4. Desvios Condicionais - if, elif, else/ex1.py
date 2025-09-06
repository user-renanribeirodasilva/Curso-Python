# Exercício 1 – Validação de acesso a plataforma
# Cenário: sistema de login com regras simples
# Regras:
# - O usuário pode acessar se tiver idade >= 18
# - Se tiver idade < 18, mostrar que o acesso é negado

# ESCREVA SEU CÓDIGO AQUI

idade = 17

if idade >= 18:
    print('Acesso liberado')
else:
    print(f'Você tem {idade}. Acesso negado')