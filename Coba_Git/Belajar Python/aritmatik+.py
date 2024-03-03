import cv2
import numpy as np

# load dua gambar dengan ukuran yang sama
img1 = cv2.imread('Foto1.jpg')
img2 = cv2.imread('Foto2.jpg')
img3 = cv2.imread('Foto3.jpg')


cv2.imshow('Original image 1', img1)
cv2.imshow('Original image 2', img2)
cv2.imshow('Original image 3', img3)

# Menambahkan kedua gambar
result = cv2.add(img1, img2, img3)



# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
