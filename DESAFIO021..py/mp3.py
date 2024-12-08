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
    sleep(3)

def reproduzir():
    tempo
    print('Reproduzindo La Amistad')
    pygame.init()
    pygame.mixer.music.load('a.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
    

elif musica ==  '2':
    tempo
    print('Reproduzindo Por Gerações - Coral Cap')
    pygame.init()
    pygame.mixer.music.load('p.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
 

elif musica == '3':
    tempo
    print('Reproduzindo Calmaria - Cata Vento')
    pygame.init()
    pygame.mixer.music.load('c.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

elif musica == '4':
    tempo 
    print('Reproduzindo Se ele não For o Primeiro')
    