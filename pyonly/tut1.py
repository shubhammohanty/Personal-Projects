import cv2

img = cv2.imread('fruits.jpg', 0)     #0 is grayscale, 1 is coloured, 2 is HSV
cv2.imshow('sample', img)
#cv2.imwrite('samplecopy.png', img)
#print('height of image is ', img.shape[0])
#print('width of image is ', img.shape[1])
#print(img.shape)

ret, bw = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  #this converts the image into binary image ie black and white image. we assigned threshold that pixels with val less than 128 are black and more than it are white.
cv2.imshow('Binary image', bw)           

cv2.waitKey(0)
cv2.destroyAllWindows()


