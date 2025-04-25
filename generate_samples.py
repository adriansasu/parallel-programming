from PIL import Image, ImageDraw
import os
import random

os.makedirs("input_images", exist_ok=True)

for i in range(10):  # You can change the number
    img = Image.new("RGB", (512, 512), (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), f"Image {i+1}", fill=(0, 0, 0))
    img.save(f"input_images/sample_{i+1}.jpg")

print("✅ Sample images generated in 'input_images/'.")
