from PIL import Image


im = Image.open("Рианна.jpg")


def mirror(im):
    pixels = im.load()
    x, y = im.size
    mirrored = Image.new('RGB', (x, y), (0, 0, 0))
    for i in range(x):
        for j in range(y):
            mirrored.putpixel((i, j), pixels[x - i - 1, j])
            mirrored.putpixel((x - i - 1, j), pixels[i, j])
    mirrored.save('mirror.jpg')


mirror(im)