import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/tousifkhan/Desktop/SEM5/DSIP_PRACT/Experiments/Experiment_9/trees.png') # Note: Update path for your Mac

# Convert BGR to RGB for correct color rendering in Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the Gaussian kernel for smoothing
kernel_size = (5, 5)
sigma = 1.5
gaussian_kernel = cv2.getGaussianKernel(kernel_size[0], sigma)
gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)

# Apply Gaussian smoothing
smoothed_image = cv2.filter2D(image_rgb, -1, gaussian_kernel)

# Define a sharpening kernel
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

# Apply sharpening
sharpened_image = cv2.filter2D(image_rgb, -1, sharpening_kernel)

# Plot using Matplotlib
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title('Original')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Smoothed')
plt.imshow(smoothed_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sharpened')
plt.imshow(sharpened_image)
plt.axis('off')

plt.tight_layout()
plt.show()