import pygame
print("Hello from lesson 14_15_16")

# Task 1

running = True
while running:

    for event in pygame.event.game():
        if event.type == pygame.QUIT:
            runnning = False
    pygame.display.flip()
pygame.quit


