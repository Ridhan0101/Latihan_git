from PIL import Image
from PIL import ImageEnhance
import cv2

# Menginput Gambar dari folder
test = Image.open("harimau-malaya.png")

# menampilkan gambar
test.show()

# Mempertajam Sebuah Gambar
Sharpnes = ImageEnhance.Sharpness(test)

Factor = 10
output = Sharpnes.enhance(Factor)
output.show()
