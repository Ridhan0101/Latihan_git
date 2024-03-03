import cv2

# load gambar dalam mode BGR
img = cv2.imread('Foto10.jpg')

# ubah gambar menjadi grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# menampilkan gambar grayscale dan menunggu input keyboard
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', img_gray)
cv2.waitKey(0)

# membersihkan jendela
cv2.destroyAllWindows()
