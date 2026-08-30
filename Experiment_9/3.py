import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/tousifkhan/Desktop/SEM5/DSIP_PRACT/Experiments/Experiment_9/trees.png')

# Convert BGR (OpenCV default) to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the size of the median filter kernel (should be an odd number)
kernel_size = 5  # You can adjust the size based on the desired smoothing level

# Apply the Median filter for smoothing
smoothed_image = cv2.medianBlur(image_rgb, kernel_size)

# Display the original and smoothed images using Matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Smoothed Image (Median Filter)')
plt.imshow(smoothed_image)
plt.axis('off')

plt.tight_layout()
plt.show()