from turtle import window_height, window_width
import pygame, sys

pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Jeu de Vaisseaux")
# import des images
ship_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/ship.png").convert_alpha()
# convert_alpha quand le sprite ne couvre pas toute la surface
background_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/background.png").convert() 

while True: # garde le jeu ouvert

    # 1. inputs (click, mouse movement, etc) --> events dans pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # cliq sur la croix de la fenetre de jeu
            pygame.quit()
            sys.exit() # pour sortir du code sans ça erreur car la boucle continue
    # 2. updates
    display_surface.fill((0,0,0))
    display_surface.blit(background_surface,(0,0))
    display_surface.blit(ship_surface,(50,500))

    
    # 3. afficher l'image
    pygame.display.update()