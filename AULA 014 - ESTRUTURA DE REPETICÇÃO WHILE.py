'''for c in range(1,5):
    n = int(input('Digite um valor: '))
print('fim')'''
'''n = 1
while n != 0:
    n = int(input(f'Digite um valor: '))
print('FIM')'''

'''r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [s/n] ')).lower()
print('FIM')

#While serve para gerar repetições indeterminadas'''

n = 1  # inicia a variavel n

#Agrega um valor às variaveis impar e par:
par = impar = 0

while n != 0: #Enquanto n for diferente de 0:

    n = int(input('Digite um valor: '))
    if n != 0: # se n for diferente de 0:

        if n % 2 == 0: # se o resto da divisão de n for igual a 0, temos X numeros pares
            par += 1

        else: #se não, temos mais 1 numero impar
            impar += 1

print(f'Voce digitou {par} numeros pares e {impar} numeros ìmpares')