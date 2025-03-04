import numpy as np
from PIL import Image
import os

# Load the image using PIL (Ensure it's RGB)
img_path = 'E:/Developer/Pythonhomeworks/lesson-14/homeworks/gray_img.jpg'

if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image file not found: {img_path}")

img_pil = Image.open(img_path).convert('RGB')
img = np.array(img_pil)

# Flip the image horizontally
img_flip_horizontal = np.fliplr(img)

# Flip the image vertically
img_flip_vertical = np.flipud(img)

# Add random noise to the image (Ensure correct dtype handling)
noise = np.random.randint(0, 50, img.shape, dtype='uint8')
img_noisy = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

# Increase the brightness of the red channel by 40
img_bright = img.copy()
img_bright[:, :, 0] = np.clip(img_bright[:, :, 0].astype(np.int16) + 40, 0, 255).astype(np.uint8)

# Apply a mask to a 100x100 area in the center
mask_size = 100
center_x, center_y = img.shape[1] // 2, img.shape[0] // 2
img_masked = img.copy()
img_masked[center_y - mask_size // 2:center_y + mask_size // 2,
           center_x - mask_size // 2:center_x + mask_size // 2] = 0

# Convert numpy arrays back to images using PIL and save them
Image.fromarray(img_flip_horizontal).save('img_flip_horizontal.jpg')
Image.fromarray(img_flip_vertical).save('img_flip_vertical.jpg')
Image.fromarray(img_noisy).save('img_noisy.jpg')
Image.fromarray(img_bright).save('img_bright.jpg')
Image.fromarray(img_masked).save('img_masked.jpg')

print("All image manipulations completed and saved successfully.")
