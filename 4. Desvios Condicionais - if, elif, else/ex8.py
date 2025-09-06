# Exercício 8 – Elegibilidade para programa VIP
# Cenário: sistema de avaliação de membros para um programa VIP
# Regras:
# - Um usuário é elegível se:
#    1. É maior de idade (idade >= 18) OU é membro premium
#    2. Não possui pendências financeiras
#    3. Tem assinatura ativa

# ESCREVA SEU CÓDIGO AQUI

idade = 18
membro = 'premium'.lower()
pendencia_financeira = False
assinatura_ativa = True

if (idade >= 18 or membro == 'premium') and not pendencia_financeira and assinatura_ativa:
    print('Acesso VIP')
else:
    print('Acesso comum')