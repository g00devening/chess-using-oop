import pygame

try:
    num = input()
    assert num.isdigit()
except:
    print('wrong!!!')
    exit()

num = int(num)
pygame.init()
size = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rhombus')
screen.fill(pygame.Color('yellow'))
while pygame.event.wait().type != pygame.QUIT:
    for i in range(300 // num):
        for j in range(300 // num):
            rhombus = [
                (i * num, (j + 1) * num - num / 2),
                ((i + 1) * num - num / 2, (j + 1) * num),
                ((i + 1) * num, (j + 1) * num - num / 2),
                ((i + 1) * num - num / 2, j * num)
            ]
            pygame.draw.polygon(screen, pygame.Color('orange'), rhombus)
    pygame.display.flip()

pygame.quit()