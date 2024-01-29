
import pygame
#import constants for the game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update game state here

            # Draw everything here
            self.screen.fill((0, 0, 0))  # Fill the screen with black

            pygame.display.flip()  # Update the full display Surface to the screen
            self.clock.tick(FPS)  # Ensure the game runs at the specified frames per second

# Wz will add other methods and logic for the snake, food, etc., here.
