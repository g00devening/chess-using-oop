from PIL import Image


def makeanaglyph(filename, delta):
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    new_im = Image.new('RGB', (x, y))
    for i in range(x):
        if i + delta >= x:
            break
        for j in range(y):
            r, g, b = pixels[i, j]
            r_new, g_new, b_new = pixels[i + delta, j]
            new_im.putpixel((i, j), (r, g_new, b_new))
    new_im.save('anaglyph.jpg')


makeanaglyph('Рианна.jpg', 10)