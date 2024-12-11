from colorama import Fore, Style

num = int(input(f'{Fore.LIGHTMAGENTA_EX}Me diga um numero qualquer: {Style.RESET_ALL}'))
if num % 2 == 0:
    print(f'O numero {num} é {Fore.BLUE}PAR{Style.RESET_ALL}')
else:
    print(f'O numero {num} é {Fore.BLUE}IMPAR{Style.RESET_ALL}')
