import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

rect_width = 120
rect_height = 80

rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2

font = pygame.font.SysFont("Times New Roman", 30)
text = font.render("Say Hi to bob the rectangle!", True, BLACK)

text_rect = text.get_rect(center=(rect_x + rect_width // 2,
                                  rect_y + rect_height // 2))

running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    screen.blit(text, (180, 50))

    pygame.display.update()

pygame.quit()
sys.exit()