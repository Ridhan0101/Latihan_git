import cv2
import numpy as np

# load gambar
img = cv2.imread('Foto8.jpg')


# mengubah tipe data gambar menjadi float32
img_float32 = np.float32(img)

# menambahkan nilai ke semua piksel untuk mencerahkan gambar
brightness = 50
img_brightened = cv2.add(img_float32, brightness)

# Mengurangi nilai ke semua pixel untuk di gelapkan gambar
darkness = 50
img_darkened = cv2.subtract(img_float32, darkness)

# mengubah tipe data gambar kembali menjadi uint8
img_brightened = np.uint8(img_brightened)
img_darkened = np.uint8(img_darkened)

# menampilkan gambar asli dan gambar yang sudah dicerahkan
cv2.imshow('Original Image', img)
cv2.imshow('Brightened Image', img_brightened)
cv2.imshow('Darkened Image', img_darkened)

# menunggu input keyboard untuk keluar
cv2.waitKey(0)

# membersihkan jendela
cv2.destroyAllWindows()
