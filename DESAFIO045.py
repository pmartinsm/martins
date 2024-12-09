import random
import time
pc = str(random.randint(1,3))
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
jogador = str(input('Qual é a sua jogada? '))
if jogador not in ['1','2','3']:
    print('Opção invalida')
else:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')

    if pc == jogador:
        resultado = 'IMPATE'

    elif (pc == '1' and jogador == '2') or (pc == '3' and jogador == '1') or (pc == '2' and jogador == '3'):
        resultado = 'JOGADOR VENCE!'
    else:
        resultado = 'COMPUTADOR VENCE!'

    jogadas = {'1':'PEDRA', '2':'PAPEL', '3':'TESOURA'}
    print(f'''{11 * '-='}
O computador jogou {jogadas[pc]}
O jogador jogou {jogadas[jogador]}
{11 * '-='}
{resultado}
''')