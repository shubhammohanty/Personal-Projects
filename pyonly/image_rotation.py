import cv2

img = cv2.imread('fruits.jpg')

height = img.shape[0]
width = img.shape[1]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 120, 0.9)          #((width, height), degree of rotation, scaling factor)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))

transposed_image = cv2.transpose(img)

cv2.imshow('original', img)
cv2.imshow('rotated', rotated_image)
cv2.imshow('transposed', transposed_image)

cv2.waitKey(0)
cv2. destroyAllWindows()