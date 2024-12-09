
from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que voce deseja: '))
#radians = radians(angulo)
#seno = sin(radians)
#cos = cos(radians)
#tan = tan(radians)
#print(f'''O angulo de {angulo} tem o SENO de {seno:.2f}
#O angulo de {angulo} tem o COSSENO  de {cos:.2f}
#O angulo de {angulo} tem a tangente de {tan:.2f} ''')

#or:
print(f'''O valor de {angulo} tem o SENO de {sin(radians(angulo)):.2f}
O valor de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}
O valor de {angulo} tem a tangente de {tan(radians(angulo)):.2f}''')
