import pygame

print('Ouça o professor Clóvis de Barros nos dizendo que nos falta brio')
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/gatin/OneDrive/Documentos/github/Exercicios_python/Audios/Clovis.mp3")
pygame.mixer.music.play()

input('Pressione enter para finalizar.')