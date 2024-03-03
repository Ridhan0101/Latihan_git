import cv2
import numpy as np

# load gambar
img = cv2.imread('Foto1.jpg')

# operasi bitwise NOT pada gambar
result = cv2.bitwise_not(img)

# tampilkan hasil
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
