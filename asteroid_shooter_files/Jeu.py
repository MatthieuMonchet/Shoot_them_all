import pygame, sys

# game init
pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Jeu de Vaisseaux")
clock = pygame.time.Clock()

# import du vaisseau
ship_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/ship.png").convert_alpha()
# convert_alpha quand le sprite ne couvre pas toute la surface
ship_rect = ship_surface.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

# import du laser
laser_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/laser.png").convert_alpha()
laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)

# import du background
background_surface = pygame.image.load(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/background.png").convert() 

# import de la police
font = pygame.font.Font(r"../Jeu de vaisseaux/asteroid_shooter_files/project_2 - Surfaces/graphics/subatomic.ttf",50)
text_font = font.render("SPACE",True,(255,255,255))
text_rect = text_font.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT-80))

while True: # garde le jeu ouvert
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clic sur la croix de la fenetre de jeu
            pygame.quit()
            sys.exit() # pour sortir du code sans ça erreur car la boucle continue
 
    # On bride le framerate
    clock.tick(60) 

    # mouse control
    ship_rect.center = pygame.mouse.get_pos()

    # 2. updates
    laser_rect.y -= 4

    # création de l'affichage
    display_surface.fill((0,0,0))
    display_surface.blit(background_surface,(0,0))
    display_surface.blit(ship_surface,ship_rect)
    display_surface.blit(laser_surface,laser_rect)
    display_surface.blit(text_font,text_rect)


    
    # 3. afficher l'image
    pygame.display.update()