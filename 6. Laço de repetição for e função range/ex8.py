# Exercício 8 – Menu interativo de operações
# Cenário: criar um console simples que executa ações até o usuário optar por sair
# Regras:
# - Exiba um menu com opções: (1) Somar, (2) Subtrair, (3) Multiplicar, (4) Dividir, (0) Sair
# - Quando a opção exigir cálculo, solicite dois números inteiros ao usuário
# - Use while para manter o programa rodando até que a opção 0 seja escolhida
# - Use if/elif/else para tratar cada opção
# - Exiba o resultado com f-strings
# - Trate divisão por zero exibindo uma mensagem apropriada (sem try/except por enquanto)
# - Se a opção for inválida, informe e volte ao menu
# - Ao sair, mostre a mensagem: "Programa encerrado"

# ESCREVA SEU CÓDIGO AQUI

opcoes = int(input('Escolha uma das opções:\n(1) Somar, (2) Subtrair, (3) Multiplicar, (4) Dividir, (0) Sair\n'))

while opcoes != 0:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    if opcoes == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcoes == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    elif opcoes == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcoes == 4:
        if n2 != 0:
            print(f'{n1} / {n2} = {n1 / n2}')
        else:
            print('Erro: divisão por zero')
    else:
        print('Opção inválida')

    opcoes = int(input('Escolha uma das opções:\n(1) Somar, (2) Subtrair, (3) Multiplicar, (4) Dividir, (0) Sair\n'))

print('Programa encerrado')