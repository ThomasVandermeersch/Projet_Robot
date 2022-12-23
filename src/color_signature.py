import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("images_test/IMG_2617.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift1 = cv2.SIFT_create(150)
sift2 = cv2.SIFT_create()
kp1, des1 = sift1.detectAndCompute(img, None)
kp2, des2 = sift2.detectAndCompute(img, None)

print(np.shape(des1))
print(np.shape(des2))