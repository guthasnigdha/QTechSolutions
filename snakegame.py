import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and food size
BLOCK_SIZE = 10
clock = pygame.time.Clock()

# Snake initial position
snake = [(100, 100)]
direction = "RIGHT"

# Food position
food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
        random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
    
    # Move snake
    x, y = snake[0]
    if direction == "UP":
        y -= BLOCK_SIZE
    elif direction == "DOWN":
        y += BLOCK_SIZE
    elif direction == "LEFT":
        x -= BLOCK_SIZE
    elif direction == "RIGHT":
        x += BLOCK_SIZE
    
    # Check collision
    if (x, y) in snake or x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
        running = False  # Game over
    
    # Update snake
    snake.insert(0, (x, y))
    if (x, y) == food:
        score += 1
        food = (random.randint(0, WIDTH//BLOCK_SIZE - 1) * BLOCK_SIZE,
                random.randint(0, HEIGHT//BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        snake.pop()
    
    # Draw snake and food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control speed

pygame.quit()
