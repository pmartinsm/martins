import pygame
from colorama import Fore, Style
from time import sleep
musica = input(f'''\n{Fore.BLUE}Escolha uma destas musicas para ouvir:'
[1] La Amistad - Dúo Zinmrah'
[2] Por Gerações - Coral CAP
[3] Calmaria - Cata Vento
[4] Se Ele Não For o Primeiro - Atautos do Rei
[5] Onisciêcia - Gabriel Tavela     
{Style.RESET_ALL}''').lower()

def tempo():
    sleep(2)

def reproduzir(nome_musica, arquivo):
    pygame.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


if musica == '1':
    reproduzir('La Amistad - Duo Zinmrah','a.mp3')
elif musica == '2':
    reproduzir('Por Gerações - Coral CAP', 'a.mp3')
elif musica == '3':
    reproduzir('Calamria - Cata Vento','c.mp3')
    

