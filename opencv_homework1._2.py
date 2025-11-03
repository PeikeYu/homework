import numpy as np
import matplotlib.pyplot as plt
import cv2
def create_gaussian_kernel(size, sigma):
    center = size // 2
    kernel = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i, j] = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)
    return kernel
def create_opencv_gaussian_kernel(size, sigma):
    kx = cv2.getGaussianKernel(size, sigma)
    return np.multiply(kx, np.transpose(kx))
def plot_kernels(kernel1, kernel2, title1, title2):
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    axs[0].imshow(kernel1, cmap='viridis', aspect='equal')
    axs[0].set_title(title1)
    axs[0].axis('off')
    axs[1].imshow(kernel2, cmap='viridis', aspect='equal')
    axs[1].set_title(title2)
    axs[1].axis('off')
    plt.tight_layout()
    plt.show()
params = [
    (3, 0.8),
    (5, 1.0),
    (7, 1.5)
]

for size, sigma in params:
    manual_kernel = create_gaussian_kernel(size, sigma)
    opencv_kernel = create_opencv_gaussian_kernel(size, sigma)
    plot_kernels(manual_kernel, opencv_kernel,
                 f"我的实现 (size={size}, σ={sigma})",
                 f"OpenCV生成 (size={size}, σ={sigma})")