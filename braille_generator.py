from PIL import Image, ImageDraw, ImageFilter

scale = 2

word = [
    [[0, 0], [0, 0], [0, 1]],
    [[0, 1], [1, 0], [1, 0]],
    [[1, 1], [0, 0], [0, 0]],
    [[0, 1], [1, 0], [0, 0]],
    [[1, 0], [0, 1], [0, 0]],
    [[1, 1], [0, 1], [1, 0]],
    [[1, 1], [0, 0], [0, 0]],
    [[1, 0], [0, 1], [0, 0]],
    [[0, 0], [0, 0], [0, 0]],
    [[0, 1], [1, 0], [0, 0]],
    [[1, 1], [0, 1], [1, 0]],
    [[0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 1]],
    [[1, 0], [1, 0], [0, 0]],
    [[1, 0], [1, 1], [1, 0]],
    [[1, 0], [0, 0], [0, 0]],
    [[0, 1], [1, 0], [0, 0]],
    [[1, 0], [1, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]],
    [[1, 0], [0, 1], [0, 0]],
]

im = Image.new('RGB', ((16 + 60 * len(word)) * scale, 79 * scale), (128, 128, 128, 0))
im.putalpha(0)

draw: ImageDraw = ImageDraw.Draw(im)


def draw_dots(d: ImageDraw, x_offset, draw_points: list):
    for i in range(3):
        for j in range(2):
            if draw_points[i][j]:
                right_x = x_offset + 24 * scale * j
                top_y = 8 * scale + 24 * scale * i
                d.ellipse((right_x, top_y, right_x + 15 * scale, top_y + 15 * scale), fill=(255, 255, 255))


for i in range(len(word)):
    draw_dots(draw, 8 * scale + i * 60 * scale, word[i])

im = im.filter(ImageFilter.GaussianBlur(1))

im.save('example.png')
