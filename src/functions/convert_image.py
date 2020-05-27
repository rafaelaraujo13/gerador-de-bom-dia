import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
from textwrap3 import wrap

dir = os.path.dirname(__file__)

def convert_image(sentence):
    # Break text
    sentence = wrap(sentence, 20)

    # Load image and font
    img = Image.open(os.path.join(dir, '../', 'images', 'original.png'))
    font = ImageFont.truetype(os.path.join(dir, '../', 'assets', 'Pangolin-Regular.ttf'), 65)

    # Manipulate image
    converted = img.resize((800, 800))
    converted = converted.filter(ImageFilter.GaussianBlur)
    enhancer = ImageEnhance.Brightness(converted)
    converted = enhancer.enhance(0.5)

    # Insert text into image
    draw = ImageDraw.Draw(converted)

    text_total_height = 0

    for line in sentence:
	    line_x_size, line_y_size = draw.textsize(line, font=font)
	    text_total_height += line_y_size

    current_height = (800 - text_total_height) / 2

    for line in sentence:
	    line_x_size, line_y_size = draw.textsize(line, font=font)
	    draw.text((((800 - line_x_size) / 2), current_height), line, fill="white", font=font)
	    current_height += line_y_size

    # Save final image
    converted.save(os.path.join(dir, '../', 'images', 'converted.png'))
