# Exercício 4 – Validação de acesso VIP em um sistema
# Cenário: sistema de benefícios premium
# Regras:
# - O usuário pode acessar se:
#    1. Possuir assinatura ativa (assinatura = True)
#    2. E (ter mais de 5 anos de cadastro OU ter desempenho excepcional)
#    3. E NÃO estiver suspenso (suspenso = False)

# ESCREVA SEU CÓDIGO AQUI
assinatura =  True
anos_cadastro = 5
desempenho_excepcional= False
suspenso = False

validacao = assinatura and (anos_cadastro >= 5 or desempenho_excepcional) and not suspenso

print(f'Acesso VITP: {validacao}')