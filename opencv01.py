# imread and imwrite image

#imread() method return a matrix

import cv2

print("hello")

img = cv2.imread("C:\\Users\\LaptopTCC\\Desktop\\em.png", 1)

#cv2.imshow('image', img)

status = cv2.imwrite("C:\\Users\\LaptopTCC\\Desktop\\em.png", 0, img)

print(status)

# display image util press a key
cv2.waitKey(0)

