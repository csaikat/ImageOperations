import cv2
import numpy as np

def add_temporal_noise(image, num_frames=5, mean=0, std=50):
    height, width, channels = image.shape
    noisy_frames = []

    for _ in range(num_frames):
        # Generate Gaussian noise for each frame
        noise_frame = np.random.normal(mean, std, (height, width, channels))

        # Make sure pixel values are within the valid range (0-255 for uint8 images)
        noisy_frame = np.clip(image + noise_frame, 0, 255).astype(np.uint8)

        # Append the noisy frame to the list
        noisy_frames.append(noisy_frame)

    return noisy_frames

# Read the image
image = cv2.imread('bhaktapur durbar_small.jpg', cv2.IMREAD_COLOR)

# Add temporal noise to the image (e.g., 10 noisy frames)
noisy_frames = add_temporal_noise(image, num_frames=5)

# Display the original and noisy frames
cv2.imshow('Original Image', image)

for i, noisy_frame in enumerate(noisy_frames):
    cv2.imwrite(f'Noisy Frame {i+1}.jpg', noisy_frame)
#     cv2.waitKey(500)  # Display each frame for 500 milliseconds (adjust as needed)
#
# cv2.destroyAllWindows()
