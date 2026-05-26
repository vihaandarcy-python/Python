import random
import pygame

SCREEN_WIDTH, SCREEN_HIEGHT = 500, 400
MOVEMENT_Speed = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load(""), (SCREEN_WIDTH, SCREEN_HIEGHT))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, hight, width):
        super().__init__()
        self.image = pygame.Surface([width, hight])
        self.image.fill(pygame.Color('dodgerblue'))

        pygame.draw.rect(self.image, color,pygame.Rect(0, 0, width, hight))
        self.rect = self.image.get_rect()

    def move(self, x_xhange, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
    
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HIEGHT - self.rect.hieht), 0)

Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, SCREEN_WIDTH- sprite1.rect.width), random.randint(0, SCREEN_HIGHT - sprite1.rect.hight)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, SCREEN_WIDTH - sprite2.rect.width), random.randint(0, SCREEN_HIGHT - sprite2.rect.hight)
all_sprites.add(sprite2)


running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressses()
        x_change = (keys[pygame.K_RIGHT] - (keys[pygame.K_LEFT])) * MOVEMENT_Speed

        y_change = (keys[pygame.K_DOWN] - (keys[pygame.K_UP])) * MOVEMENT_Speed

        sprite1.move(x_change, y_change)

        if sprite1.rect.coliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    Screen.blit(background_image, (0, 0))
    all_sprites.draw(Screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        Screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HIEGHT - win_text.get_height()) // 2))

        pygame.display.flip()
        clock.tick(90)

pygame.quit()

        
