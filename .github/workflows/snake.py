from PIL import Image, ImageDraw
import numpy as np

def generate_snake():
    # Generate a simple image (replace this with your own logic)
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10,10), "Snake graph", fill=(0,0,0))

    # Save the image
    img.save('dist/github-contribution-grid-snake.png')

if __name__ == "__main__":
    generate_snake()
