# Exercício 4 – Validação de acesso VIP
# Cenário: sistema de clube VIP
# Regras:
# - O usuário pode ter acesso VIP se:
#    1. Tiver mais de 18 anos OU for membro premium
#    2. E não estiver com pendências financeiras

# ESCREVA SEU CÓDIGO AQUI
idade = 17
membro_premium = True
pendencia_financeira = False

if (idade >= 18 or membro_premium) and not pendencia_financeira:
    print(f'Acesso VIP liberado. ')
else:
    print(f'Infelizmenete você não esta apto')