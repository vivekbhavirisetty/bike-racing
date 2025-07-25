import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bike Racing Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load images
bike_img = pygame.image.load("bike.png")  # Place a 50x100 bike.png in the same directory
bike_img = pygame.transform.scale(bike_img, (50, 100))

# Bike settings
bike_x = WIDTH // 2 - 25
bike_y = HEIGHT - 120
bike_speed = 10

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 8
obstacles = []

def draw_bike(x, y):
    screen.blit(bike_img, (x, y))

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

def check_collision(bike_rect, obstacles):
    for obs in obstacles:
        if bike_rect.colliderect(obs):
            return True
    return False

def main():
    global bike_x
    score = 0
    running = True

    while running:
        screen.fill(GREEN)
        pygame.draw.rect(screen, ROAD_COLOR, (150, 0, 300, HEIGHT))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key press
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bike_x > 150:
            bike_x -= bike_speed
        if keys[pygame.K_RIGHT] and bike_x < 400:
            bike_x += bike_speed

        # Add obstacles
        if random.randint(0, 30) == 0:
            x_pos = random.choice([175, 250, 325])  # Three lanes
            obstacles.append(pygame.Rect(x_pos, -100, obstacle_width, obstacle_height))

        # Move obstacles
        for obs in obstacles:
            obs.y += obstacle_speed

        # Remove off-screen obstacles
        obstacles[:] = [obs for obs in obstacles if obs.y < HEIGHT]

        # Draw
        draw_bike(bike_x, bike_y)
        draw_obstacles(obstacles)

        # Collision
        bike_rect = pygame.Rect(bike_x, bike_y, 50, 100)
        if check_collision(bike_rect, obstacles):
            font = pygame.font.SysFont(None, 75)
            game_over = font.render("Game Over", True, RED)
            screen.blit(game_over, (180, 300))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        # Update score
        score += 1
        font = pygame.font.SysFont(None, 40)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(30)

main()