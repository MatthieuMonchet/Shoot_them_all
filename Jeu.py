from turtle import window_height, window_width
import pygame, sys

pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

while True: # garde le jeu ouvert

    # 1. inputs (click, mouse movement, etc) --> events dans pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # cliq sur la croix de la fenetre de jeu
            pygame.quit()
            sys.exit() # pour sortir du code sans ça erreur car la boucle continue
    # 2. updates
    # 3. afficher l'image
    pygame.display.update()