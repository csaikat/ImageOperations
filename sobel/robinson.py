import cv2
import numpy as np

image1 = cv2.imread('bhaktapur durbar_small.jpg', cv2.IMREAD_GRAYSCALE)

n = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
nw = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
w = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
sw = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
s = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
se = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])
e = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
ne = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])



convolved = cv2.filter2D(src=image1,ddepth= -1, kernel=n)


cv2.imwrite('robin_north.jpg', convolved)
