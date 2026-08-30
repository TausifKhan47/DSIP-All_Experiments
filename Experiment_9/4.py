import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/tousifkhan/Desktop/SEM5/DSIP_PRACT/Experiments/Experiment_9/trees.png')

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian smoothing to reduce noise
blurred_image = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# Create a Laplacian kernel for sharpening
laplacian_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]], dtype=np.float32)

# Apply the Laplacian filter for sharpening
sharpened_image = cv2.filter2D(blurred_image, -1, laplacian_kernel)

# Display the original, blurred, and sharpened images using Matplotlib
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Blurred Image (Gaussian)')
plt.imshow(blurred_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sharpened Image (Laplacian)')
plt.imshow(sharpened_image)
plt.axis('off')

plt.tight_layout()
plt.show()