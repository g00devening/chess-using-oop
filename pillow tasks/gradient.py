from PIL import Image


def gradient(color):
    red = color == 'R'
    green = color == 'G'
    blue = color == 'B'
    new = Image.new('RGB', (512, 200), (0, 0, 0))
    for i in range(0, 512, 2):
        for j in range(200):
            new.putpixel((i, j), (red * i // 2, green * i // 2, blue * i // 2))
            new.putpixel((i + 1, j), (red * i // 2, green * i // 2, blue * i // 2))
    new.save('gradient.jpg')


gradient('B')