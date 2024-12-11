preco = ''
km = int(input('Qual a distancia da sua viagem? '))
if km <= 200:
    preco = km * 0.50
elif km > 200:
    preco = km * 0.45

print(f"""Você está prestes a começar uma viagem de {km:.1f}KM.
E o preço da sua passagem será de {preco:.2f}""")

