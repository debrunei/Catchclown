import pygame, random
pygame.init()

Window_Width = 945
Window_Height = 600
FPS = 60
clock = pygame.time.Clock()

pygame.display.set_mode(Window_Width, Window_Height)
pygame.display.set_caption("Catch the clown")

PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1
score = 0
player_live = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

font = pygame.font.Font("assets/Franxurter.ttf", 32)

BLUE = (1,175, 209)
YELLOW = (248, 23, 28)

