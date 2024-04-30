import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Coin Collector")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game objects
player_width = 50
player_height = 50
player_x = window_width / 2 - player_width / 2
player_y = window_height - player_height - 50
player_speed = 5
coin_radius = 15
coin_x = random.randint(coin_radius, window_width - coin_radius)
coin_y = -coin_radius
coin_speed = 3
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5
score = 0
font = pygame.font.SysFont(None, 30)
game_over = False

# Set up the background
background_color = (0, 0, 0)

# Set up the title
title_font = pygame.font.SysFont(None, 50)
title_text = title_font.render("Coin Collector", True, (255, 255, 255))
title_x = window_width / 2 - title_text.get_width() / 2
title_y = 10

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
    
    # Update the game objects
    if not game_over:
        coin_y += coin_speed
        if coin_y > window_height:
            coin_x = random.randint(coin_radius, window_width - coin_radius)
            coin_y = -coin_radius
            score += 1
        
        obstacle_y += obstacle_speed
        if obstacle_y > window_height:
            obstacle_x = random.randint(0, window_width - obstacle_width)
            obstacle_y = -obstacle_height
        
        # Check for collisions
        if player_x < coin_x + coin_radius and player_x + player_width > coin_x - coin_radius and player_y < coin_y + coin_radius and player_y + player_height > coin_y - coin_radius:
            coin_x = random.randint(coin_radius, window_width - coin_radius)
            coin_y = -coin_radius
            score += 1
        
        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            game_over = True
    
    # Draw the game objects
    window.fill(background_color)
    pygame.draw.rect(window, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.draw.circle(window, (255, 255, 0), (coin_x, coin_y), coin_radius)
    pygame.draw.rect(window, (0, 0, 255), (player_x, player_y, player_width, player_height))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(game_over_text, (window_width / 2 - game_over_text.get_width() / 2, window_height / 2 - game_over_text.get_height() / 2))
    
    window.blit(title_text, (title_x, title_y))
    pygame.display.update()
    
    # Limit the frame rate
    clock.tick(60)
    
# Clean up
pygame.quit()
