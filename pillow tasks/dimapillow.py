from PIL import Image, ImageDraw


im = Image.open("Рианна.jpg")
pixels = im.load()
x, y = im.size
reds = []
greens = []
blues = []
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        reds.append(r)
        greens.append(g)
        blues.append(b)
avg_r, avg_g, avg_b = sum(reds) // len(reds), sum(greens) // len(greens), sum(blues) // len(blues)
avg_im = Image.new("RGB", (x, y), (avg_r, avg_g, avg_b))
avg_im.save('average_image.png')