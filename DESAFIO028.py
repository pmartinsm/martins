from colorama import Fore, Style
from random import randint
from time import sleep

pc = randint(1,5)
print(f"""{Fore.LIGHTYELLOW_EX}{25 * '-=-'}{Style.RESET_ALL}
{Fore.BLUE}Vou pensar em um número entre 0 e 5. Tente advinhar...{Style.RESET_ALL}
{Fore.LIGHTYELLOW_EX}{25 * '-=-'}{Style.RESET_ALL}""")

jogador = int(input('Em qual numero pensei? '))
if jogador != pc:
    print(f'{Fore.LIGHTMAGENTA_EX}PROCESSANDO...{Style.RESET_ALL}')
    sleep(1)
    print(f'{Fore.RED}GANHEI! Eu pensei no número {pc} e não no {jogador}!{Style.RESET_ALL}')

else:
    print(f'{Fore.YELLOW}PARABENS! Você conseguiu me vencer!{Style.RESET_ALL}')

