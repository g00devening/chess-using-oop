import pygame

try:
    width, num = [x for x in input().split()]
    assert num.isdigit() and width.isdigit()
except:
    print('wrong!!!')
    exit()

width = int(width)
num = int(num)
pygame.init()
size = 2*width*num, 2*width*num
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Target')
screen.fill((0, 0, 0))
while pygame.event.wait().type != pygame.QUIT:
    for i in range(num):
        if i % 3 == 0:
            color = (255, 0, 0)
        elif i % 3 == 1:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        pygame.draw.circle(screen, color, (width * num, width * num), width * (num - i))
    pygame.display.flip()

pygame.quit()