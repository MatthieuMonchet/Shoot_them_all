from this import s
import pygame, sys

pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Jeu de Vaisseaux")
clock = pygame.time.Clock()
# import des images
ship_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/ship.png").convert_alpha()
ship_rect = ship_surface.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
# convert_alpha quand le sprite ne couvre pas toute la surface
background_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/background.png").convert() 
# import de la police
font = pygame.font.Font(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/subatomic.ttf",50)
text_font = font.render("SPACE",True,(255,255,255))
text_rect = text_font.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT))
while True: # garde le jeu ouvert

    # 1. inputs (click, mouse movement, etc) --> events dans pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clic sur la croix de la fenetre de jeu
            pygame.quit()
            sys.exit() # pour sortir du code sans ça erreur car la boucle continue
    clock.tick(60) # On bride le framerate
    # 2. updates
    display_surface.fill((0,0,0))
    display_surface.blit(background_surface,(0,0))
    if ship_rect.top > 0:
        ship_rect.y -= 4
    display_surface.blit(ship_surface,ship_rect)
    display_surface.blit(text_font,text_rect)


    
    # 3. afficher l'image
    pygame.display.update()