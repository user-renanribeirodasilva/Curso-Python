# Exercício 5 – Validação de promoção em um sistema corporativo
# Cenário: empresa quer conceder uma promoção especial aos funcionários
# Regras:
# - O funcionário só recebe a promoção se:
#    1. Tem mais de 2 anos de empresa OU é gerente
#    2. E não tem advertência pendente
#    3. E tem avaliação de desempenho >= 8

# ESCREVA SEU CÓDIGO AQUI
anos_empresa =  2
gerente = True
advertencia = False
desempenho = 8.3

validacao = (anos_empresa >= 2 or gerente) and not advertencia and desempenho >= 8
print(f'Promoção: {validacao}')