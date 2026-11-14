import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
import player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt : float = 0.0
    Player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #Game loop
    while True:
        log_state()
        #Event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Screen rendering
        screen.fill("black")
        Player.update(dt)
        Player.draw(screen)
        pygame.display.flip()

        #Delta time calculation
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
