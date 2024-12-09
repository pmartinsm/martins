from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que a ano a {pessoa}° pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
         totmaior += 1
    else:
        totmenor += 1
print(f'''Ao todos tivemos {totmaior} pessoas maiores de idade.
E tambem tivemos {totmenor} menores de idade.''')






