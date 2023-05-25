from PIL import Image


im = Image.open("Рианна.jpg")


def diagonal(im):
    pixels = im.load()
    x, y = im.size
    diagonalized = Image.new('RGB', (x, y), (0, 0, 0))
    for i in range(x):
        for j in range(y):
            diagonalized.putpixel((i, j), pixels[x - i - 1, y - j - 1])
            diagonalized.putpixel((x - i - 1, y - j - 1), pixels[i, j])
    diagonalized.save('diagonal.jpg')


diagonal(im)