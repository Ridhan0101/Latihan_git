from PIL import Image

# Membuka gambar
test = Image.open("harimau-malaya.png")

# Mengambil nilai pixel pada posisi x = 50, y = 100
pixel = test.getpixel((100, 100))

# Menampilkan nilai pixel
print(pixel)
