import pygame
print("Hello from lesson 14_15_16")

# Task 1

pygame.init()
screenW = 800
screenH = 600
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Pong Game")

white = (255, 255, 255)
green = (0, 153, 0)

paddleW = 20
paddleH = 100

paddle1X = 10
paddle1Y = (screenH // 2) - (paddleH // 2)

paddle2X = (screenW - paddleW - 10)
paddle2Y = (screenH // 2) - (paddleH // 2)

ballR = 10
ballX = screenW // 2
ballY = screenH // 2

running = True
while running:
    screen.fill(green)
    pygame.draw.rect(screen, white, (paddle1X, paddle1Y, paddleW, paddleH))
    pygame.draw.rect(screen, white, (paddle2X, paddle2Y, paddleW, paddleH))
    pygame.draw.circle(screen, white, ())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1Y > 0:
        paddle1Y = paddle1Y - 1
    if keys[pygame.K_s] and paddle1Y < screenH - paddleH:
        paddle1Y = paddle1Y + 1
    if keys[pygame.K_UP] and paddle2Y > 0:
        paddle2Y = paddle2Y - 1
    if keys[pygame.K_DOWN] and paddle2Y < screenH - paddleH:
        paddle2Y = paddle2Y + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


