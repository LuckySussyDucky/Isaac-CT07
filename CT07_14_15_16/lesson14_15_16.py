import pygame
print("Hello from lesson 14_15_16")

# Task 1

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")



running = True
while running:
    for event in pygame.event.game():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


