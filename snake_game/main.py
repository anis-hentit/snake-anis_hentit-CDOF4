# main.py
import pygame
import sys
from game import Game

def main():
    pygame.init()  # Initialize all pygame modules
    game = Game()
    game.run()
    pygame.quit()  # Uninitialize all pygame modules
    sys.exit()

if __name__ == "__main__":
    main()
