lista_de_compras = []

for i in range(3):
    item_usuario = input(f'Digite um item para adicionar na lista {i+1}: ')
    lista_de_compras.append(item_usuario)

print(f'O total da lista ficou assim: {lista_de_compras}')