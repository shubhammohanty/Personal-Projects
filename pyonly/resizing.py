import cv2
img = cv2.imread('fruits.jpg')

resized = cv2.resize(img, None, fx=1.5, fy=1.5)
resized_by_resolution = cv2.resize(img, (480, 480), interpolation=cv2.INTER_AREA)

cv2.imshow('resized image', resized)
cv2.imshow('original image', img)
cv2.imshow('resized image by resolution', resized_by_resolution)

cv2.waitKey(0)
cv2. destroyAllWindows()