# Exercício 6 – Classificação escolar
# Cenário: sistema de avaliação de alunos
# Regras:
# - O usuário deve informar a média do aluno (float)
# - Classifique o aluno da seguinte forma:
#    - Média >= 9: "Excelente"
#    - Média >= 7 e < 9: "Bom"
#    - Média >= 5 e < 7: "Regular"
#    - Média < 5: "Insatisfatório"

# ESCREVA SEU CÓDIGO AQUI

media = float(input('Digite a média do aluno: '))

if media >= 9:
    print(f'Excelente. Média: {media}')
elif 7 <= media < 9:
    print(f'Bom. Média: {media}')
elif 5 <= media < 7:
    print(f'Regular. Média: {media}')
else:
    print(f'Insatisfatório. Média: {media}')