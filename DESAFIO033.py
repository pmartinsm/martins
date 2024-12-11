a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
#verificando quem é maior:
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
