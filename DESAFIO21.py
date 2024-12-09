import pygame
musica = input('Escolha uma destas musicas para ouvir:'
               'Amistad - Dúo Zinmrah'
               'Por Gerações - Coral CAP'
               '').lower()
if 'amistad' in musica:
    pygame.init()
    pygame.mixer.music.load('amistad.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
elif 'dead pool' in musica:
    print('Não temos essa opção!')


