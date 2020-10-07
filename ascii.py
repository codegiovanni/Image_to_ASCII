from PIL import Image, ImageDraw, ImageFont

# chars = " .:-=+*#%@"
chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

char_width = 18
char_height = 18

img = Image.open('enter_name.jpg')

WIDTH, HEIGHT = img.size
img = img.resize((int(WIDTH / char_width), int(HEIGHT / char_height)), Image.NEAREST)
width, height = img.size
img = img.load()

ascii_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))

fnt = ImageFont.truetype('C:/Windows/Fonts/BRITANIC.ttf', 20)

d = ImageDraw.Draw(ascii_img)


def getChar(value):
    return chars[int(value * (len(chars) / 256))]


for i in range(height):
    for j in range(width):
        r, g, b = img[j, i]
        k = int((r + g + b) / 3)
        d.text((j * char_width, i * char_height), getChar(k), font=fnt, fill=(r, g, b))

ascii_img.save('enter_output_name.png')

