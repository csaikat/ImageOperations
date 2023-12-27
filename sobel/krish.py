import numpy as np
import  cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('bhaktapur durbar.jpg',0)


#East

import scipy
from scipy import ndimage

e_k = np.zeros_like(img)
ka= np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])

e_k=ndimage.convolve(img,ka,mode='nearest',cval=0.0)
cv.imwrite('East_image_krish.jpg',e_k)

# s_k = np.zeros_like(img)
# n_k = np.zeros_like(img)
# nw_k = np.zeros_like(img)
# ne_k = np.zeros_like(img)
# sw_k = np.zeros_like(img)
# se_k = np.zeros_like(img)
# w_k = np.zeros_like(img)
#
# na= np.array([[-3,-3,5],[-3,0,5],[-3,-3,5]])
# wa= np.array([[5,5,5],[-3,0,-3],[-3,-3,-3]])
# sa= np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
# nea= np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])
# nwa= np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
# sea= np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
# swa= np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
# n_k = ndimage.convolve(img, na, mode='nearest', cval=0.0)
#
# s_k = ndimage.convolve(img, sa, mode='nearest', cval=0.0)
#
# w_k = ndimage.convolve(img, wa, mode='nearest', cval=0.0)
#
# ne_k = ndimage.convolve(img, nea, mode='nearest', cval=0.0)
#
# nw_k = ndimage.convolve(img, nwa, mode='nearest', cval=0.0)
#
# se_k = ndimage.convolve(img, sea, mode='nearest', cval=0.0)
#
# sw_k = ndimage.convolve(img, swa, mode='nearest', cval=0.0)
#
# cv.imwrite('East_image_krish.jpg',e_k)
# cv.imwrite('north_image_krish.jpg',na)
# cv.imwrite('west_image_krish.jpg',wa)
# cv.imwrite('south_image_krish.jpg',sa)
# cv.imwrite('NorthEast_image_krish.jpg',nea)
# cv.imwrite('NorthWest_image_krish.jpg',nwa)
# cv.imwrite('SouthEast_image_krish.jpg',sea)
# cv.imwrite('SouthWest_image_krish.jpg',swa)