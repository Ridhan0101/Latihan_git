from PIL import Image
from PIL import ImageEnhance

# menginput gambar dari folder
test = Image.open("harimau-malaya.png")

# menampilkan gambar awal
test.show("Gambar Awal")

# mencerahkan gambar dan meredupkan gambar
brightnes = ImageEnhance.Brightness(test)

# Meredupkan Gambar
factor = 0.5
im_output = brightnes.enhance(factor)
im_output.show("Brightnes -")

# Mencerahkan Gambar
factor = 1.5
im_output = brightnes.enhance(factor)
im_output.show("Brightnes +")
