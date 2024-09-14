from PIL import Image

ascii_chars = " .~:-=+*#%@"

width = 100

image = Image.open("images/snowl2.jpg")
height = int(width * image.height // image.width * 0.5)
image = image.resize((width, height))

for y in range(height):
    for x in range(width):
        r, g, b, = image.getpixel((x, y))
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        index = int(gray / 256 * len(ascii_chars))
        print(ascii_chars[index], end="")
    print()