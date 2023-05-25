from PIL import Image, ImageDraw


def board(num, size):
    brd = Image.new('RGB', (num * size, num * size))
    for i in range(num):
        for j in range(num):
            draw = ImageDraw.Draw(brd)
            if (i + j) % 2 == 0:
                draw.rectangle([(i * size, j * size), ((i + 1) * size, (j + 1) * size)], fill=(255, 255, 255))
            else:
                draw.rectangle([(i * size, j * size), ((i + 1) * size, (j + 1) * size)], fill=(0, 0, 0))
    brd.save('board.jpg')


board(8, 50)