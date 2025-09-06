# Exercício 10 – Tempo de Viagem
# 1. Crie variáveis para distância em km e velocidade média em km/h
# 2. Calcule o tempo de viagem em horas (tempo = distância / velocidade)
# 3. Mostre a frase: "Para percorrer 150 km a 50 km/h, serão necessárias 3.0 horas", formatando com 1 casa decimal

# ESCREVA SEU CÓDIGO AQUI

distancia_km = 1000
velocidade_media = 70

tempo_viagem = (distancia_km / velocidade_media)

print(f'Para percorrer {distancia_km} km a {velocidade_media} km/h, serão necessárias {tempo_viagem:.1f} horas')