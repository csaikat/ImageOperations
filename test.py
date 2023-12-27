import cv2
import numpy as np
image = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
robinson_masks = [
    np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),    # G1
    np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]),    # G2
    np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),    # G3
    np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]]),    # G4
    np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),    # G5
    np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]),    # G6
    np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),    # G7
    np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])     # G8
]
def apply_robinson_masks(image):
    result = np.zeros_like(image, dtype=float)
    for mask in robinson_masks:
        convolved = cv2.filter2D(src=image,ddepth= -1, kernel=mask)
        result = np.maximum(result, convolved)
    return result

robinson_edges = apply_robinson_masks(image)
robinson_edges = np.clip(robinson_edges, 0, 255).astype(np.uint8)
cv2.imwrite("Robinson Edges.jpg", robinson_edges)
