import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER1_COLOR = (255, 0, 0)  # Red
PLAYER2_COLOR = (0, 0, 255)  # Blue
HOOK_SIZE = 20
FISH_SIZE = 20

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the players
player1_x, player1_y = 100, HEIGHT // 2
player2_x, player2_y = WIDTH - 100, HEIGHT // 2

# Set up the fish
fish_x, fish_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
fish_speed_x, fish_speed_y = random.choice([-2, 2]), random.choice([-2, 2])

# Set up the hooks
hook1_x, hook1_y = player1_x + 50, player1_y
hook2_x, hook2_y = player2_x - 50, player2_y

# Load the hook image
hook_image = pygame.image.load('images/hook.png')
hook_image = pygame.transform.scale(hook_image, (HOOK_SIZE, HOOK_SIZE))

# Set up the score
score1, score2 = 0, 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move player 1
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5
    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5

    # Move player 2
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5

    # Move the hooks
    hook1_x, hook1_y = player1_x + 50, player1_y
    hook2_x, hook2_y = player2_x - 50, player2_y

    # Move the fish
    fish_x += fish_speed_x
    fish_y += fish_speed_y

    # Bounce the fish off the edges
    if fish_x < 0 or fish_x > WIDTH:
        fish_speed_x *= -1
    if fish_y < 0 or fish_y > HEIGHT:
        fish_speed_y *= -1

    # Check for collisions
    if (hook1_x - FISH_SIZE < fish_x < hook1_x + HOOK_SIZE and
            hook1_y - FISH_SIZE < fish_y < hook1_y + HOOK_SIZE):
        score1 += 1
        fish_x, fish_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    if (hook2_x - FISH_SIZE < fish_x < hook2_x + HOOK_SIZE and
            hook2_y - FISH_SIZE < fish_y < hook2_y + HOOK_SIZE):
        score2 += 1
        fish_x, fish_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, PLAYER1_COLOR, (player1_x, player1_y), (hook1_x, hook1_y), 5)
    pygame.draw.line(screen, PLAYER2_COLOR, (player2_x, player2_y), (hook2_x, hook2_y), 5)
    screen.blit(hook_image, (hook1_x, hook1_y))
    screen.blit(hook_image, (hook2_x, hook2_y))
    pygame.draw.rect(screen, (255, 255, 0), (fish_x, fish_y, FISH_SIZE, FISH_SIZE))
    text = font.render(f"Score: {score1} - {score2}", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame