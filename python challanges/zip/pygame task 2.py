import pygame
pygame.init()

Grey = (58, 58, 58)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((500, 500))

pygame.display.set_caption('My First Game Screen')

image = pygame.image.load('image.png')

DEFAULT_IMAGE_SIZE = (300, 210)

image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

x = 500/2-300//2

y = 500/2-210//2

print(f"x  {x} y {y}") 


DEFAULT_IMAGE_POSITION = (x, y)

while True:
    display_surface.fill(Grey)
    display_surface.blit(image, DEFAULT_IMAGE_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()


    pygame.display.flip()
    clock.tick(30)