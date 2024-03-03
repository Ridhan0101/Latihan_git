from PIL import Image
from PIL import ImageFilter

# Menginput Gambar dari Folder
test = Image.open("harimau-malaya.png")

# menampilkan Gambar Awal
test.show()


contour = test.filter(ImageFilter.CONTOUR)
contour.show()
