soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    soma = soma + num
    cont = cont + 1
print(f'Voce informou {cont} e a soma foi {soma}')