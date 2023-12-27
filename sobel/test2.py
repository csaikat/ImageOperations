# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# image= cv2.imread("bhaktapur durbar_small.jpg", cv2.IMREAD_GRAYSCALE)
# robinson_masks = [
#     np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),    # G1
#     np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]),    # G2
#     np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),    # G3
#     np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]]),    # G4
#     np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),    # G5
#     np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]),    # G6
#     np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),    # G7
#     np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])     # G8
# ]
# def apply_robinson_masks(image):
#     result = np.zeros_like(image, dtype=float)
#     for mask in robinson_masks:
#         convolved = cv2.filter2D(src=image,ddepth= -1, kernel=mask)
#         result = np.maximum(result, convolved)
#     return result
#
# robinson_edges = apply_robinson_masks(image)
# robinson_edges = np.clip(robinson_edges, 0, 255).astype(np.uint8)
# cv2.imwrite("Robinson Edges.jpg", robinson_edges)
import matplotlib.image as img
import numpy as np
from matplotlib import pyplot as plt
image_path = 'C:\\Users\\Saikat Chatterjee\\OneDrive\\Desktop\\Image operations\\bhaktapur durbar_small.jpg'  # Replace 'path_to_your_image.jpg' with the actual path to your image file
ipimage = img.imread(image_path)

from scipy import ndimage

e_k = np.zeros_like(ipimage)
#For east
ka= np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
e_k=ndimage.convolve(ipimage,ka,mode='nearest',cval=0.0)
plt.imshow(e_k)
plt.xticks([]),plt.yticks([])
plt.show()