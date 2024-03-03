from PIL import Image

# Menginput Gambar dari Folder
test = Image.open("harimau-malaya.png")

# Menampilkan Gambar Awal
test.show()

# Memutar Gambar

# Memutar gambar sebanyak 180 Derajat
Rotate = test.rotate(180)
Rotate.show()

# Memutar gambar sebanyak 200 Derajat
Rotate = test.rotate(200)
Rotate.show()

# Memutar gambar sebanyak 90 Derajat
Rotate = test.rotate(90)
Rotate.show()
