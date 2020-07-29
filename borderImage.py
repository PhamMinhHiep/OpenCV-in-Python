
import cv2

import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img = cv2.imread(r'C:\Users\LaptopTCC\Desktop\cat.jpg')
replicate = cv2.copyMakeBorder(img, 100, 100 ,100, 10, cv2.BORDER_REPLICATE)
plt.subplot(231), plt.imshow(img,'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('Replicate')
plt.show() 