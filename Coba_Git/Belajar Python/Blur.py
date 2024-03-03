from PIL import Image
from PIL import ImageFilter
import cv2


# Menginput Gambar dari Folder
test = Image.open("harimau-malaya.png")

# Menampilkan Gambar Awal
test.show()

# Membuat gambar menjadi kabur
# Membuat gambar blur
blur = test.filter(ImageFilter.BLUR)
blur.show("Blur")


