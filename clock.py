import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("mickey_clock.png")
background = pygame.transform.scale(background, (width, height))

minute_hand = pygame.image.load("minute_hand.png")
minute_hand = pygame.transform.scale(minute_hand, (500, 160))

second_hand = pygame.image.load("second_hand.png")
second_hand = pygame.transform.scale(second_hand, (500, 160))

center_x = width // 2 
center_y = height // 2 

minute_hand_rect = minute_hand.get_rect(center=(center_x, center_y))
second_hand_rect = second_hand.get_rect(center=(center_x, center_y))

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=pos).center)
    surf.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -(minutes + seconds / 60) * 6
    second_angle = -seconds * 6

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    blit_rotate_center(screen, minute_hand, (170, 300), minute_angle)
    blit_rotate_center(screen, second_hand, (200, 300), second_angle)

    pygame.display.flip()
    pygame.time.Clock().tick(60)


#через центр картинки, но выходит неровно
'''import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("mickey_clock.png")
background = pygame.transform.scale(background, (width, height))

minute_hand = pygame.image.load("minute_hand.png")
minute_hand = pygame.transform.scale(minute_hand, (500, 160))

second_hand = pygame.image.load("second_hand.png")
second_hand = pygame.transform.scale(second_hand, (500, 160))

center_x, center_y = width // 2, height // 2

def blit_rotate_center(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    new_rect.center = pos
    return rotated_image, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -(minutes + seconds / 60) * 6
    second_angle = -seconds * 6

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    minute_hand_rect = minute_hand.get_rect(center=(center_x, center_y))
    rotated_minute_hand, rotated_minute_rect = blit_rotate_center(screen, minute_hand, (center_x, center_y), minute_angle)
    screen.blit(rotated_minute_hand, rotated_minute_rect.topleft)

    second_hand_rect = second_hand.get_rect(center=(center_x, center_y))
    rotated_second_hand, rotated_second_rect = blit_rotate_center(screen, second_hand, (center_x, center_y), second_angle)
    screen.blit(rotated_second_hand, rotated_second_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
'''