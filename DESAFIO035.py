print(f'''{20 * '-='}
Analisador de triângulos
{20 * '-='}''')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORAR um triângulo!')
else:
    print('Os egmentos acima NÂO PODEM FORMAR um triângulo!')