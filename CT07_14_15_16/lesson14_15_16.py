import pygame
print("Hello from lesson 14_15_16")

# Task 1

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

white = (255, 255, 255)
paddleW = 20
paddleH = 100
paddle1X = 10
paddle1Y = (screen_height // 2) - (paddleH // 2)
paddle2X = 
paddle2Y = (screen_height // 2) - (paddleH // 2)

running = True
while running:
    pygame.draw.rect(screen, white, (paddle1X, paddle1Y, paddleW, paddleH))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


