'''
Nyiss egy terminált:
    Vagy beírod hogy cmd a keresőbe és rányomsz arra ami felugrik, vagy
    Visual studioban bal fent Go mellett "..." -> "Terminal" -> New terminal
    Ennek a shortcutja egyébként Ctrl+Shift+ő

    Ha ez megvan, írd be ezt a sort:
    pip install pygame
'''

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
pygame.display.set_caption("Rios játék")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game objects
player_width = 50
player_height = 50
player_x = window_width / 2 - player_width / 2
player_y = window_height - player_height
player_speed = 5
bird_size = 40
bird_x = random.randint(bird_size, window_width - bird_size)
bird_y = -bird_size
bird_speed = 3
obstacle_width = 100
obstacle_height = 20
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5
score = 0
lives = 3
font = pygame.font.SysFont(None, 30)
game_over = False

# Set up the background
background_image = pygame.image.load('kepek/hatter.jpg')

# Set up the player
player_image = pygame.image.load('kepek/jatekos.png')
player_image = pygame.transform.scale(player_image, (player_width, player_height))

# Set up the bird object
bird_image = pygame.image.load('kepek/madar.png')
bird_image = pygame.transform.scale(bird_image, (bird_size, bird_size))

# Set up the obstacle object
obstacle_image = pygame.image.load('kepek/akadaly.png')
obstacle_image = pygame.transform.scale(obstacle_image, (obstacle_width, obstacle_height))

# Set up the life panel
life_font = pygame.font.SysFont(None, 30)
life_text = life_font.render("hátralévő életek: " + str(lives), True, (255, 255, 255))
life_panel_x = window_width - life_text.get_width() - 10
life_panel_y = 10

# Set up the score panel
score_font = pygame.font.SysFont(None, 30)
score_text = score_font.render("pontszám: " + str(score), True, (255, 255, 255))
score_panel_x = 10
score_panel_y = 10

# Main game loop
while not game_over:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep the player within the border
    if player_x < 0:
        player_x = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width

    # Move the bird
    bird_y += bird_speed

    # Move the obstacle
    obstacle_y += obstacle_speed

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    bird_rect = pygame.Rect(bird_x, bird_y, bird_size, bird_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if pygame.Rect.colliderect(player_rect, bird_rect):
        score += 1
        bird_x = random.randint(bird_size, window_width - bird_size)
        bird_y = -bird_size
    elif pygame.Rect.colliderect(player_rect, obstacle_rect):
        lives -= 1
        if lives == 0:
            game_over = True
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = -obstacle_height

    # Check if the bird is off the screen
    if bird_y > window_height:
        bird_x = random.randint(bird_size, window_width - bird_size)
        bird_y = -bird_size

    # Check if the obstacle is off the screen
    if obstacle_y > window_height:
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = -obstacle_height

    # Update the life panel
    life_text = life_font.render("hátralévő életek: " + str(lives), True, (255, 255, 255))

    # Update the score text
    score_text = score_font.render("pontszám: " + str(score), True, (255, 255, 255))

    # Draw everything
    window.blit(background_image, (0, 0))
    window.blit(player_image, (player_x, player_y))
    window.blit(bird_image, (bird_x, bird_y))
    window.blit(obstacle_image, (obstacle_x, obstacle_y))
    window.blit(life_text, (life_panel_x, life_panel_y))
    window.blit(score_text, (score_panel_x, score_panel_y))
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Print the final score and number of lives
print("elért pontszám: " + str(score))
print("hátralévő életek: " + str(lives))

# Exit the game
pygame.quit()