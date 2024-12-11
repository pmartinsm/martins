from colorama import Fore, Style

atual = float(input('Qual é o salário do fucionário? R$'))
# para fucionarios com salarios inferiores ou igual a 1250:
if atual <= 1250:
    novo = (atual * 15 / 100) + atual
#para fucionarios com salarios superiores a 1250:
else:
    novo = (atual * 10 / 100) + atual
print(f'Quem ganhava {Fore.RED}R${atual:.2f}{Style.RESET_ALL} passa a ganhar {Fore.BLUE}R${novo:.2f}{Style.RESET_ALL} agora.')
