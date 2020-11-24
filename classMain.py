import cv2
import numpy as np
img = cv2.imread('input.png',1)
cv2.imshow('Image_hull',img)
cv2.waitKey(0)
cv2.destroyAllWindows()