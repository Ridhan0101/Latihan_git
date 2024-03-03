from PIL import Image
from PIL import ImageFilter

# Menginput Gambar dari Folder
test = Image.open("harimau-malaya.png")

# menampilkan Gambar Awal
test.show()

# Membuat Gambar Smoth
Smoth = test.convert()
Smoth = Smoth.filter(ImageFilter.SMOOTH_MORE)
Smoth.show("Smoth")


