import pygame

def main():

    pygame.display.init()
    screen = pygame.display.set_mode((1200, 900))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
