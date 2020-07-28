# get pixel value

import numpy as np

import cv2

img = cv2.imread("C:\\Users\\LaptopTCC\\Desktop\\em.png", 1)

pixel = img[100,100]

print(pixel)