import cv2
import numpy as np
identity=np.array([[0,0,0],[0,1,0],[0,0,0]])
img = cv2.imread('bhaktapur durbar.jpg')
im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY,identity)

# cv2.imwrite('identity_image.jpg',img2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
cv2.imwrite('image_guss.jpg',img_gaussian)
#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])


img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img2=img_prewitty+img_prewittx

# cv2.imwrite('x_image.jpg',img_prewittx)
# cv2.imwrite('y_image.jpg',img_prewitty )
cv2.imwrite('prewitt_image.jpg',img2)
# closing all open windows
# cv2.destroyAllWindows()