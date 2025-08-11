# **Desafio Adicional: Calculadora de Custo de Frete**

# **Problema:**
# Um sistema de e-commerce calcula o valor do frete com base na região de destino do cliente e no tipo de entrega escolhido (Padrão ou Expresso).

# **As regras são:**
# 1.  Para a região **Sudeste**, o frete Padrão custa R$ 12,00 e o Expresso custa R$ 20,00.
# 2.  Para a região **Sul**, o frete Padrão custa R$ 15,00 e o Expresso custa R$ 28,00.
# 3.  Para as regiões **Norte** ou **Nordeste** (ambas têm o mesmo valor), o frete Padrão custa R$ 25,00 e o Expresso custa R$ 45,00.
# 4.  Para a região **Centro-Oeste**, o frete Padrão custa R$ 18,00 e o Expresso custa R$ 35,00.

# **Sua tarefa:**
# Escreva um programa interativo que pergunte ao usuário para qual **região** o pacote será enviado e qual o **tipo de entrega**. As regiões válidas são `Sudeste`, `Sul`, `Norte`, `Nordeste`, `Centro-Oeste`. Os tipos de entrega válidos são `Padrão` e `Expresso`.

# O programa deve calcular e imprimir o valor final do frete. Se o usuário digitar uma região ou tipo de entrega inválido, o programa deve imprimir uma mensagem de erro apropriada.

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
