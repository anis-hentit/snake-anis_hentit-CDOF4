
import pygame
#import constants for the game
from constants import *






class Snake:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]  # Start in the middle of the screen
        self.direction = (SNAKE_SPEED, 0)  # Start direction: right as a vector
        self.grow_to = 0  # When the snake eats food, this will increase

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        # Check if the new direction is not the opposite of the current direction
        if self.length() > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return  # Prevent the snake from turning back on itself
        else:
            self.direction = point # Change the direction

    def move(self):
        cur = self.get_head_position() # Get the current position of the snake's head
        x, y = self.direction # Get the direction of the snake
        new = (((cur[0] + x) % SCREEN_WIDTH), (cur[1] + y) % SCREEN_HEIGHT) # Calculate the new position of the snake's head
        if len(self.positions) > 2 and new in self.positions[2:]: # Check for self collision
            self.reset()  # Reset the snake
        else:
            self.positions.insert(0, new) # Insert the new position of the snake's head
            if self.grow_to > 0: # Check if the snake has eaten food
                self.grow_to -= 1 # Decrease the number of blocks to grow
            else:
                self.positions.pop() # Remove the last block of the snake

    def reset(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (SNAKE_SPEED, 0)  # Reset direction to right
        self.grow_to = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (SNAKE_SIZE, SNAKE_SIZE)) # Create a rectangle for each block of the snake
            pygame.draw.rect(surface, WHITE, r)# Draw the rectangle on the screen
            pygame.draw.rect(surface, GREEN, r, 1)# Draw the outline of the rectangle on the screen

    def length(self):
        return len(self.positions)

    def grow(self):
        self.grow_to += 1






class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock() # Create a clock to control the game's frame rate
        self.snake = Snake()
        self.food = None
        self.spawn_food()

    def spawn_food(self): # Spawn food at a random location
        import random
        self.food = (random.randint(0, (SCREEN_WIDTH-FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                     random.randint(0, (SCREEN_HEIGHT-FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)

    def check_eat_food(self): # Check if the snake has eaten food
        if self.snake.get_head_position() == self.food:
            self.snake.grow()
            self.spawn_food()

    def run(self): # Run the game	
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.turn((0, -SNAKE_SIZE))
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn((0, SNAKE_SIZE))
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn((-SNAKE_SIZE, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn((SNAKE_SIZE, 0))

            self.snake.move()
            self.check_eat_food()

            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.draw_food()

            pygame.display.flip() # Update the full display Surface to the screen
            self.clock.tick(FPS) # Limit the game's frame rate

    def draw_food(self): # Draw the food on the screen
        food_rect = pygame.Rect((self.food[0], self.food[1]), (FOOD_SIZE, FOOD_SIZE))
        pygame.draw.rect(self.screen, RED, food_rect)
