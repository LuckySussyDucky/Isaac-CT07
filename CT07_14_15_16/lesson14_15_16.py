import pygame
print("Hello from lesson 14_15_16")

# Task 1

pygame.init()
screenW = 800
screenHheight = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

white = (255, 255, 255)
paddleW = 20
paddleH = 100
paddle1X = 10
paddle1Y = (screen_height // 2) - (paddleH // 2)
paddle2X = (screen_width - paddleW - 10)
paddle2Y = (screen_height // 2) - (paddleH // 2)

running = True
while running:
    pygame.draw.rect(screen, white, (paddle1X, paddle1Y, paddleW, paddleH))
    pygame.draw.rect(screen, white, (paddle2X, paddle2Y, paddleW, paddleH))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1Y > 0:
        paddle1Y = paddle1Y - 1
    if keys[pygame.K_s] and paddle1Y < screenH:
        paddle1Y = paddle1Y + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


