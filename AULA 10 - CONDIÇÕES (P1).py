'''nome = str(input('Qual é seu nome? ')).lower()
if nome == 'pedro': # cira uma condção, executando o
    # codigo apenas se a parte de cima for igual aquilo especificado.

    print('Que nome bonito!') # como está dentro do laço, o print
    # acontece somente se o nome for pedro.

#apenas com if, estrutura de condicional simples, quando tem else
# se torna estrutura de condcional composta

else: #= se não
    print(f'Bom dia, {nome}')'''

"""print(f'Bom dia, {nome}') # ja esse print, está fora do laço, sendo assim
#acontece independente do nome."""


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >=6.0 : # se a media for = ou maior a 6.0:
    """print('sua média foi boa, PARABÉNS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')"""

    print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS!')


















