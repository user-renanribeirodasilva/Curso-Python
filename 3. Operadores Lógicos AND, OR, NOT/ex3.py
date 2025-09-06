# Exercício 3 
# Cenário: sistema de benefícios para funcionários
# Regras:
# - O funcionário recebe um bônus se:
#    1. Trabalha mais de 40 horas semanais OU tem desempenho excelente
#    2. NÃO está em período de advertência

# ESCREVA SEU CÓDIGO AQUI

horas_semanais = 40
desempenho_excepcional = True
advertencia = False

validacao = (horas_semanais >= 40 or desempenho_excepcional) and not advertencia 

print(f'Tem direito ao beneficio: {validacao}')

