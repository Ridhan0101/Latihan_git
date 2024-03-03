import cv2
import numpy as np

img = cv2.imread('Foto1.jpg', 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur', blur)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
