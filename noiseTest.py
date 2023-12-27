import numpy as np
import cv2

# read input image
img = cv2.imread('bhaktapur durbar_small.jpg')
z = img.reshape((-1,3))

# convert to np.float32
z = np.float32(z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imwrite("Quant_pic.jpg",res2)
# display the image
# cv2.imshow('Image with K=8',res2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()