print('Faça um programa que abra e reproduza o Áudio de um arquivo MP3')

import pygame
pygame.init()
pygame.mixer.load('kalimpa.mp3')
pygame.mixer.play()
pygame.event.wait()