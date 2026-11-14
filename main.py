import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state, log_event
import player
import asteroid
from asteroidfield import AsteroidField
import sys


def main():
    #Set groups:
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player.Player.containers = (drawable,updatable)
    asteroid.Asteroid.containers = (asteroids,drawable,updatable)
    AsteroidField.containers = (updatable)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt : float = 0.0

    AsteroidField()
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
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collides_with(Player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()

        #Delta time calculation
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
