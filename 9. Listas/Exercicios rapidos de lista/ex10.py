notas = []

for nota in range(4):
    notas_digitadas = float(input('Digite uma nota: '))
    notas.append(notas_digitadas)
print(f'Total de notas inseridas: {notas}')

media = (sum(notas)/len(notas))
print(f'A média das notas foi de: {media:.2f}')

maior_nota = max(notas)
print(f'A maior nota foi: {maior_nota}')