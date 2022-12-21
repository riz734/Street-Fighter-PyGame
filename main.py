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

#sprites
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEP = [10,8,1,7,7,3,7]
WIZARD_ANIMATION_STEP = [8,8,1,8,8,3,7]

#color codes
TAN = (255,24,153)
YELL = (255,255,153)
RED = (255,0,0)

#fighter vars
WARRIOR_SIZE = 162
WARRIOR_DATA = [WARRIOR_SIZE]
WIZARD_SIZE = 250
WIZARD_DATA = [WIZARD_SIZE]


#draw background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#health bars
def draw_health_bars(health,x,y):
    ratio = health / 100
    pygame.draw.rect(screen,TAN,(x-2,y-2,405,35))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELL,(x,y,400*ratio,30))

#create two instances of fighter
fighter1 = Fighter(200,310,WARRIOR_DATA,warrior_sheet,WARRIOR_ANIMATION_STEP)
fighter2 = Fighter(700,310,WIZARD_DATA, wizard_sheet,WIZARD_ANIMATION_STEP)


#game loop, constantly running, updating until break
run = True
while run:

    clock.tick(FPS)

    #draw bg
    draw_bg()

    #move fighterr
    fighter1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter2)

    #show stats
    draw_health_bars(fighter1.health,20,20)
    draw_health_bars(fighter2.health,580,20)

    #fighter2.move()

    fighter1.draw(screen)
    fighter2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    #update display
    pygame.display.update()

pygame.quit()