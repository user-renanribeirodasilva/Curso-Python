frutas = []

for i in range (5):
    fruta = input(f'Digite uma fruta {i+1}: ')
    frutas.append(fruta)
print(f'Lista de frutas: {frutas}')

remove_fruta = input('Você deseja remover alguma fruta? s/n: ').lower()

if remove_fruta == 's':
    removendo_fruta = input('Digite o nome da fruta que deseja eliminar: ')
    if removendo_fruta in frutas:
        frutas.remove(removendo_fruta)
print(f'Lista final: {frutas}')
    


