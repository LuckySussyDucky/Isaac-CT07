import pygame
print("Hello from lesson 14_15_16")

# Task 1

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

paddleW = 20
paddleY = 100
paddle1X = 10
paddle1Y = (screen_height // 2) - (paddleY // 2)

running = True
while running:
    pygame.draw.rect(screen, (255, 255, 255), (paddle))
    for event in pygame.event.game():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


