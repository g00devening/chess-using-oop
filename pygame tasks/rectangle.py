import pygame, random

try:
    width, height = [x for x in input().split()]
    assert width.isdigit() and height.isdigit()
except:
    print('wrong!!!')
    exit()
width = int(width)
height = int(height)
pygame.init()
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rectangle')

while pygame.event.wait().type != pygame.QUIT:
    screen.fill((0, 0, 0))
    screen.fill(pygame.Color('red'), (1, 1, width - 1, height - 1))
    pygame.display.flip()


pygame.quit()