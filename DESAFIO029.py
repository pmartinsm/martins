from time import sleep
from colorama import Fore, Style

km = float(input('Qual a velocidade atual do carro? '))
if km > 80.0:
    m = (km - 80) * 7

    print(f'{Fore.BLUE}PROCESSANDO...{Style.RESET_ALL}')
    sleep(1)
    print(f'''{Fore.RED}MULTADO! Você execedeu o limite permitido que é de 80KM/h
Voce deve pagar uma multa de {m:.2f}!{Style.RESET_ALL}\n''')

print(f'{Fore.LIGHTYELLOW_EX}Tenha um bom dia! Dirija com segurança!{Style.RESET_ALL}')