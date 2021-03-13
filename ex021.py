# importando o modulo
import pygame
# iniciando o pygame e mixer
pygame.mixer.init()
# carregar o mp3
pygame.mixer.music.load('musica.mp3')
# tocar musica
pygame.mixer.music.play()
# terminar
while(pygame.mixer.music.get_busy()): pass

