import cv2
import numpy as np

img = cv2.imread('fruits.jpg')

height = img.shape[0]
width = img.shape[1]
quarter_height = img.shape[0]/4
quarter_width = img.shape[1]/4

T = np.float32([[1, 0, quarter_height], [0, 1, quarter_width]])
img_translation = cv2.warpAffine(img, T, (width, height))

cv2.imshow('original', img)
cv2.imshow('translated', img_translation)

cv2.waitKey(0)
cv2. destroyAllWindows()
