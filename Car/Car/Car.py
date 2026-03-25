import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed =  random.randint(1,10)

score = 0
game_over = False

def get_shake_offset(intensity):
    #Return a random (x, y) offset for screen shake.
    return (
        random.randint(-intensity, intensity),
        random.randint(-intensity, intensity)
    )

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Should move right

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        score += 1
        enemy_speed = enemy_speed + random.randint(1,5)
        if enemy_speed > 10000:
            enemy_speed = random.randint(20,120)
        print(f"Score: {score}",f"speed: {enemy_speed}",f"Screen Shake:{shake_intensity}")
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    # --- Collision Detection ---
    if (player_pos[0] < enemy_pos[0] + enemy_size and
        player_pos[0] + player_size > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + enemy_size and
        player_pos[1] + player_size > enemy_pos[1]):
        print("Game Over!")
        game_over = True

    # --- Screen Shake ---
    # Intensity is proportional to enemy_speed, but capped for playability
    shake_intensity = (enemy_speed + score)
    shake_x, shake_y = get_shake_offset(shake_intensity)

    # Drawing
    screen.fill((0, 0, 0))
    
    # Apply shake offset to all game objects
    pygame.draw.rect(screen, RED, (enemy_pos[0] + shake_x, enemy_pos[1] + shake_y, enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0] + shake_x, player_pos[1] + shake_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)
