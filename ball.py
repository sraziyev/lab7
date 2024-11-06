'''import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()

x, y = 250, 250
ball_radius = 25
ball_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - ball_radius - ball_speed >= 0:
                y -= ball_speed
            if event.key == pygame.K_DOWN and y + ball_radius + ball_speed <= 500:
                y += ball_speed
            if event.key == pygame.K_LEFT and x - ball_radius - ball_speed >= 0:
                x -= ball_speed
            if event.key == pygame.K_RIGHT and x + ball_radius + ball_speed <= 500:
                x += ball_speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), ball_radius)
    pygame.display.flip()
    clock.tick(60)
'''

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
x = 250
y = 250
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y - 25 > 0:
        y -= 20
    if pressed[pygame.K_DOWN] and y + 25 < 500:
        y += 20
    if pressed[pygame.K_LEFT] and x - 25 > 0:
        x -= 20
    if pressed[pygame.K_RIGHT] and x + 25 < 500:
        x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)
