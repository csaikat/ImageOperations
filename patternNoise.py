import cv2
import numpy as np

def generate_pattern_noise(shape, scale=50):
    # Create a pattern with sinusoidal noise
    x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    pattern = np.sin(x / scale) + np.sin(y / scale)

    # Normalize the pattern to the range [0, 1]
    pattern = (pattern - np.min(pattern)) / (np.max(pattern) - np.min(pattern))

    return pattern

def add_pattern_noise(image, scale=50):
    pattern = generate_pattern_noise(image.shape[:2], scale)

    # Broadcast the pattern to match the image's shape (for color channels)
    pattern = np.stack([pattern] * image.shape[2], axis=-1)

    # Add pattern noise to the image
    noisy_image = np.clip(image + pattern, 0, 255).astype(np.uint8)

    return noisy_image

# Load the image using OpenCV
image_path = 'bhaktapur durbar_small.jpg'  # Replace with the actual image path
img = cv2.imread(image_path)

# Convert the image to float32 data type in the range [0, 1]
img = img.astype(np.float32) / 255.0

# Add pattern noise to the image
scale_factor = 10  # Adjust the scale factor as needed
noisy_image = add_pattern_noise(img, scale=scale_factor)

# Convert the noisy image back to uint8 data type in the range [0, 255]
noisy_image = (noisy_image * 255).astype(np.uint8)

# Display or save the noisy image
cv2.imwrite("Noisy10.jpg", noisy_image)
# cv2.imshow("Noisy Image", noisy_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
