import pygame
from fighter import Fighter


pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#bg image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#draw background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#create two instances of fighter
fighter1 = Fighter(200,310)
fighter2 = Fighter(700,310)
#game loop
run = True
while run:

    clock.tick(FPS)

    draw_bg()

    #move fighter
    fighter1.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    #fighter2.move()

    fighter1.draw(screen)
    fighter2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    #update display
    pygame.display.update()

pygame.quit()