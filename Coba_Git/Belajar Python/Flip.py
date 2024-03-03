from PIL import Image

# Menginput gambar dari folder
test = Image.open("harimau-malaya.png")

# Menampilkan Gambar Awal
test.show()

# Membuat gambar terbalik
Flip = test.transpose(Image.FLIP_TOP_BOTTOM)
Flip.show("Flip")
