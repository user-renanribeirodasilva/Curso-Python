# Exercício 5 – Classificação de funcionário
# Cenário: sistema de avaliação de promoção
# Regras:
# - Um funcionário pode ser classificado para promoção se:
#    1. Trabalhou na empresa por pelo menos 2 anos OU é gerente
#    2. Não possui advertências
#    3. Tem desempenho igual ou superior a 8

# ESCREVA SEU CÓDIGO AQUI
anos_empresa = 2
gerente = True
advertencia = False
desempenho = 8.7

if (anos_empresa >= 2 or gerente) and not advertencia and desempenho >= 8:
    print(f'Parabéns, você possui os seguintes requisitos: tempo de empresa: {anos_empresa} anos. Gerente: {gerente}. Advertencia: {advertencia}. Nota de desempenho: {desempenho}')
else:
    print('Infelizmente você não é elegível')