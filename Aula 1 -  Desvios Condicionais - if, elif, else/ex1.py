regiao_entrega = input('Para qual região o pacote será entregue? ').lower()
tipo_entrega = input('Qual será o tipo de entrega? Padrão ou Expresso ?' ).lower()


if regiao_entrega == 'sudeste' and tipo_entrega == 'padrão':
    print('o frete padrão custa R$ 12,00')
elif regiao_entrega == 'sudeste' and tipo_entrega == 'expresso':
    print('o frete expresso custa R$ 20,00')
elif regiao_entrega == 'sul' and tipo_entrega == 'padrão':
    print('o frete padrão custa R$ 15,00')
elif regiao_entrega == 'sul' and tipo_entrega == 'expresso':
    print('o frete expresso custa R$ 28,00')
elif (regiao_entrega == 'norte' or regiao_entrega == 'nordeste') and tipo_entrega == 'padrão':
    print('o frete padrão custa R$ 25,00')
elif (regiao_entrega == 'norte' or regiao_entrega == 'nordeste') and tipo_entrega == 'expresso':
    print('o frete expresso custa R$ 45,00')
elif regiao_entrega == 'centro-oeste' and tipo_entrega == 'padrão':
    print('o frete padrão custa R$ 18,00')
elif regiao_entrega == 'centro-oeste' and tipo_entrega == 'expresso':
    print('o frete expresso custa R$ 35,00')
else:
    print('Informações invalidas.')
