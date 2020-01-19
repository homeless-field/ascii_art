# Import an image processing tool
from PIL import Image

# Decide what image to convert, and make it 1/3 the size
image = Image.open("ctycgchr36231.jpg")
image = image.resize((int(image.width / 3), int(image.height / 3)))

# Define the ASCII characters and the variables
characters = '.', '*', '$'
text = ''
a, b = 0, 0
x, y, z = 0, 0, 0

# For every pixel in the image...
while y < image.height:
# Find its brightness
    brightness = sum(image.getpixel((x, y))) / 3
# Depending on its brightness, assign it an ASCII character
    while z < 3:
        a += 85
        if brightness <= a and brightness > b:
            text += characters[z]
            text += characters[z]
        b += 85
        z += 1
    z = 0
    a = 0
    b = 0
    if x == image.width - 1:
        text += '\n'
        y += 1
        x = 0
    else:
        x += 1

#Print the output
print(text)
