from random import randint
import pygame

pc = randint(1,5)

jogador = int(input('\nPensei em um numero entre 1 e 5. Tente advinhar qual foi: '))
while jogador != pc:

    if jogador == pc:
        print('Voce ganhou')
        pygame.init()
        pygame.mixer.music.load('g.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
