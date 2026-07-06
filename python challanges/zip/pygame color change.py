import pygame
import random

pygame.init()

Sprite_Color_Change_Event = pygame.USEREVENT + 1
Background_Color_Change_Event = pygame.USEREVENT + 2

#Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

#sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, hieght, width):

        super().__init__

        self.image = pygame.Surface([width, hieght])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):

        self.rect.move.ip(self.velocity)
        boundry_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True

        if self.rect.left <= 0 or self.rect.right >= 400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True

        if boundry_hit:
            pygame.event.post(pygame.event.Event(Sprite_Color_Change_Event))
            pygame.event.post(pygame.event.Event(Background_Color_Change_Event))
    
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
    
def change_background_color():
    global bg_color 
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)

sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Boundry Sprite")

bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        elif event.type == Sprite_Color_Change_Event:


