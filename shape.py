import cv2
import numpy as np


img = np.zeros((512, 512, 3))

cv2.line(img, (0,0), (512, 512), (0, 190, 0), 1)
cv2.rectangle(img, (0,0), (300, 200), (0,120,200), 2)
cv2.circle(img, (400, 50), 30, (100, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)