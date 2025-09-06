# Exercício 3 – Verificação de categoria de nadador
# Cenário: sistema de classificação de atletas
# Regras:
# - O usuário deve informar a idade do nadador
# - Classifique o nadador nas categorias:
#    - Até 12 anos: "Infantil"
#    - De 13 a 17 anos: "Juvenil"
#    - 18 anos ou mais: "Adulto"

# ESCREVA SEU CÓDIGO AQUI
idade = int(input('Informe a idade do nadador: '))

if idade <= 12:
    print('Infantil')
elif  13 <= idade <= 17:
    print('Juvenil')
else:
    print('Adulto')