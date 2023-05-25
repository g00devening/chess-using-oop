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
pygame.display.set_caption('Sphere')
screen.fill((0, 0, 0))
while pygame.event.wait().type != pygame.QUIT:
    for i in range(1, num + 1):
        pygame.draw.ellipse(screen, (255, 255, 255), (0, 150 - i * 150 / num, 300, i * 300 / num), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (150 - i * 150 / num, 0, i * 300 / num, 300), 1)
    pygame.display.flip()

pygame.quit()