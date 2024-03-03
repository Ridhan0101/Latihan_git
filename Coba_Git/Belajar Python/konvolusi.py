import cv2
import numpy as np

# membaca gambar
img = cv2.imread('Foto1.jpg')

# mengubah gambar ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# membuat kernel blur 5x5
kernel = 1/25 * np.ones((5, 5), dtype=np.float32)

# melakukan konvolusi
blur = cv2.filter2D(gray, -1, kernel)

# menampilkan gambar asli dan hasil konvolusi
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
