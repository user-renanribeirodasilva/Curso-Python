# Exercício 7 – Elegibilidade para bônus anual
# Cenário: sistema de avaliação de funcionários
# Regras:
# - Um funcionário é elegível para bônus se:
#    1. Trabalhou na empresa há pelo menos 3 anos OU é gerente sênior
#    2. Tem nota de desempenho >= 8.5
#    3. Não possui advertências nem suspensões

# ESCREVA SEU CÓDIGO AQUI
anos_empresa = 3
gerente_senior = True
desempenho = 8.9
advertencia = False
suspenso = False

if (anos_empresa >= 3 or gerente_senior) and desempenho >= 8.5 and not advertencia and not suspenso:
    print('O funcionário atende a todos os requisitos, por isso é elegível para o bônus')
else:
    print('O funcionário não tem direito ao bônus')