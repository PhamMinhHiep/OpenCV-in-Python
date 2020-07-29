# Resize an Image with scale 0.6
import cv2

path = r'C:\Users\LaptopTCC\Desktop\cat.jpg'

img = cv2.imread(path, 1)

height = img.shape[0]
width = img.shape[1]
scale = 30
dim = (int (height * scale / 100),int (width * scale / 100))



resized = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

resize1 = cv2.resize(img, (300, 300))

# crop Image
imgCrop = img[0:200, 200:500]


cv2.imshow('resized image', resized)

cv2.imshow('resize1', resize1)

cv2.imshow('imgCrop', imgCrop)

cv2.waitKey(0)

