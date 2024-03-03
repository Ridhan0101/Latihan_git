import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('harimau-malaya.png')

print(img.shape)  # (152, 203, 3) = (tinggi, lebar, channel gambar)
print(img[0][0][2])  # mengakses pixel warna MERAH di titik paling kiri atas
print(img[0][0][1])  # mengakses pixel warna HIJAU di titik paling kiri atas
print(img[0][0][0])  # mengakses pixel warna BIRU di titik paling kiri atas
print(cv2.mean(img))

color = ('r', 'g', 'b')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
