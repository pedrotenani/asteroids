import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black color

        # Update the player
        player.update(dt)
        
        # Draw the player
        player.draw(screen)

        pygame.display.flip()   # Refresh the screen

        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS and update dt

    pygame.quit()

if __name__ == "__main__":
    main()