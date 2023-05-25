import pygame

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
pygame.display.set_caption('Cross')


while pygame.event.wait().type != pygame.QUIT:
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), width=5)
    pygame.display.flip()


pygame.quit()