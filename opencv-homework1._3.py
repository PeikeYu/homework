import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
image = Image.open("image.jpg").convert("L")
image_array = np.array(image)
def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size))
    center = size // 2
    for i in range(size):
        for j in range(size):
            x, y = i - center, j - center
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2)) / (2 * np.pi * sigma**2)
    return kernel / np.sum(kernel)
def gaussian_filter(image, kernel):
    height, width = image.shape
    k_size = kernel.shape[0]
    pad = k_size // 2
    filtered = np.zeros_like(image, dtype=np.float32)
    for i in range(pad, height-pad):
        for j in range(pad, width-pad):
            filtered[i, j] = np.sum(image[i-pad:i+pad+1, j-pad:j+pad+1] * kernel)
    return filtered
params = [
    (3, 1.0),
    (5, 1.5),
    (7, 2.0)
]
plt.figure(figsize=(15, 10))
plt.subplot(1, len(params)+1, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original')
for i, (size, sigma) in enumerate(params):
    kernel = gaussian_kernel(size, sigma)
    filtered = gaussian_filter(image_array, kernel)
    plt.subplot(1, len(params)+1, i+2)
    plt.imshow(filtered, cmap='gray')
    plt.title(f'σ={sigma}, size={size}')
plt.tight_layout()
plt.show()