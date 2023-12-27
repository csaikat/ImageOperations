import cv2
from scipy import ndimage, misc
import numpy as np
from skimage import filters, io, util
from math import pi


def laplacian_of_gaussian(self, name):
    image = ndimage.imread(name)
    l_o_g1 = ndimage.gaussian_laplace(image, sigma=0.7, mode='nearest')
    l_o_g2 = ndimage.gaussian_laplace(image, sigma=0.8, mode='nearest')
    l_o_g3 = ndimage.gaussian_laplace(image, sigma=1.0, mode='nearest')
    l_o_g4 = ndimage.gaussian_laplace(image, sigma=1.5, mode='nearest')
    l_o_g5 = ndimage.gaussian_laplace(image, sigma=2.0, mode='nearest')

    misc.imsave(str('l_o_g07_' + self.image_name), l_o_g1)
    misc.imsave(str('l_o_g08_' + self.image_name), l_o_g2)
    misc.imsave(str('l_o_g10_' + self.image_name), l_o_g3)
    misc.imsave(str('l_o_g15_' + self.image_name), l_o_g4)
    misc.imsave(str('l_o_g20_' + self.image_name), l_o_g5)



laplacian_of_gaussian('flower.jpg')
