import pygame

def main():
    pygame.init()
    screen_width, screen_hieght = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_hieght))
    pygame.display.set_caption('Color changing sprite!')

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')}
    
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_hieght = 100, 100

    clock = pygame.time.Clock()

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width-sprite_width)
        y = min(max(0, y), screen_hieght - sprite_hieght)

        if x == 0: current_color = colors['red']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['green']
        elif y == screen_hieght- sprite_hieght: current_color = colors['blue']
        else: current_color = colors['white']



        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,(x, y, sprite_width, sprite_hieght))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()

    
