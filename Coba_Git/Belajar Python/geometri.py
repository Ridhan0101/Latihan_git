import cv2
import numpy as np

img = cv2.imread('Foto5.jpg')

# Mendapatkan ukuran gambar
height, width = img.shape[:2]

# Menghitung nilai tengah gambar
center = (width/2, height/2)

# Rotasi gambar sebesar 45 derajat
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_img = cv2.warpAffine(img, M, (width, height))

# Menggeser gambar sebesar 100 piksel ke kanan dan 50 piksel ke bawah
M = np.float32([[1, 0, 100], [0, 1, 50]])
translated_img = cv2.warpAffine(img, M, (width, height))

# Flip gambar secara horizontal
flipped_img = cv2.flip(img, 1)

# Flip gambar secara vertical
flipped_img2 = cv2.flip(img, 0)

# Flip gambar secara horizontal dan vertical
flipped_img3 = cv2.flip(img, -1)

# Scaling gambar dengan faktor 1.5
scaled_img = cv2.resize(img, None, fx=1.5, fy=1.5,
                        interpolation=cv2.INTER_LINEAR)

# Cropping gambar dengan ukuran (300, 300) dan posisi (200, 100)
cropped_img = img[100:200, 200:4000]

# Menampilkan gambar asli, gambar yang dirotasi, dan gambar yang digeser
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_img)
cv2.imshow("Translated Image", translated_img)
cv2.imshow("Flip Image Horizontal", flipped_img)
cv2.imshow("Flip Image Vertical", flipped_img2)
cv2.imshow("Flip Image keduanya", flipped_img3)
cv2.imshow("Scaling ", scaled_img)
cv2.imshow("Crop", cropped_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
