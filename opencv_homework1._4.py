import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
image = Image.open("image.jpg").convert("L")
image_array = np.array(image)
def zero_padding(image, pad_size):
    height, width = image.shape
    padded = np.zeros((height + 2*pad_size, width + 2*pad_size), dtype=image.dtype)
    padded[pad_size:height+pad_size, pad_size:width+pad_size] = image
    return padded
def wrap_padding(image, pad_size):
    height, width = image.shape
    padded = np.zeros((height + 2*pad_size, width + 2*pad_size), dtype=image.dtype)
    padded[pad_size:height+pad_size, pad_size:width+pad_size] = image
    padded[:pad_size, pad_size:width+pad_size] = image[:pad_size, :][::-1, :]
    padded[height+pad_size:, pad_size:width+pad_size] = image[height-pad_size:, :][::-1, :]
    padded[:, :pad_size] = padded[:, pad_size:2*pad_size][:, ::-1]
    padded[:, width+pad_size:] = padded[:, width:width+pad_size][:, ::-1]
    return padded
pad_size = 30
zero_padded = zero_padding(image_array, pad_size)
mirror_padded = wrap_padding(image_array, pad_size)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original')
plt.subplot(1, 3, 2)
plt.imshow(zero_padded, cmap='gray')
plt.title('Zero Padding')
plt.subplot(1, 3, 3)
plt.imshow(mirror_padded, cmap='gray')
plt.title('Wrap Padding')
plt.tight_layout()
plt.show()