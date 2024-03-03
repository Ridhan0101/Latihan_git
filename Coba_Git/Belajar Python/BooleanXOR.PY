import cv2
import numpy as np

# load dua gambar dengan ukuran yang sama
img1 = cv2.imread('Foto1.jpg')
img2 = cv2.imread('Foto2.jpg')

# resize gambar agar memiliki ukuran yang sama
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# operasi bitwise XOR pada gambar
result = cv2.bitwise_xor(img1, img2)

# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
