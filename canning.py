import cv2
import numpy as np
img = cv2.imread('flower.jpg')
low_threshold =115
ratio=1.4
kernel_size=5
img_blur = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('canny_gaussianBlur.jpg',img_blur)
detected_edges = cv2.Canny(img_blur, low_threshold, low_threshold * ratio, kernel_size)
cv2.imwrite('canny_flower.jpg',detected_edges)