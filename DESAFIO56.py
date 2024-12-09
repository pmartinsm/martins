somaidade = 0
idade = 0
mediaidade = 0
idadehomem = 0
nomevelho = ''

for p in range (1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip()
    if p == 1 and sexo in 'Mm':
        somaidade += idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadehomem:
        idadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4
print(f'''A media de idade do grupo é de {mediaidade} anos.
O homem mais velho do grupo tem {idadehomem} e se chama {nomevelho}''')

