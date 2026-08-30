import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/tousifkhan/Desktop/SEM5/DSIP_PRACT/Experiments/Experiment_9/trees.png')

# Convert BGR (OpenCV default) to RGB (Matplotlib default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the size of the Averaging filter kernel
kernel_size = (5, 5)  # You can adjust the size based on the desired smoothing level

# Create the Averaging filter kernel
kernel = np.ones(kernel_size, dtype=np.float32) / (kernel_size[0] * kernel_size[1])

# Apply the Averaging filter for smoothing
smoothed_image = cv2.filter2D(image_rgb, -1, kernel)

# Display the original and smoothed images side by side using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Smoothed Image (Averaging Filter)')
plt.imshow(smoothed_image)
plt.axis('off')

plt.tight_layout()
plt.show()