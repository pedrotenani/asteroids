import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Create an asteroid field
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black color

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False
                break

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
        
        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()   # Refresh the screen

        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS and update dt

    pygame.quit()

if __name__ == "__main__":
    main()