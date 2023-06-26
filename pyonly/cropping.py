from tracemalloc import start
import cv2

img = cv2.imread('fruits.jpg')

height = img.shape[0]
width = img.shape[1]
start_row = int(height*0.25)
start_col = int(width*0.25)
end_row = int(height*0.75)
end_col = int(width*0.75)

cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow('cropped image', cropped)
cv2.imshow('original image', img)

cv2.waitKey(0)
cv2. destroyAllWindows()