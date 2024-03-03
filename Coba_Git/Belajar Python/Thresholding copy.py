import cv2
import numpy as np

# load gambar
img = cv2.imread('Foto1.jpg', 0)

# melakukan thresholding dengan nilai ambang 127
# nilai piksel yang lebih besar dari 127 akan menjadi 255 (putih), sedangkan yang lain menjadi 0 (hitam)
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# menampilkan gambar asli dan hasil thresholding
cv2.imshow('Original Image', img)
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# menunggu input keyboard untuk keluar
cv2.waitKey(0)

# membersihkan jendela
cv2.destroyAllWindows()
