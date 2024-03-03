from PIL import Image

# Membuka gambar
test = Image.open("harimau-malaya.png")

# Mendapatkan ukuran gambar
width, height = test.size

# Batas jumlah pixel yang dicari nilainya
limit = 100

# Variabel counter untuk menghitung jumlah pixel yang sudah dicari nilainya
counter = 0

# Perulangan untuk mengambil nilai pixel dari setiap pixel
for y in range(height):
    for x in range(width):
        # Mengambil nilai pixel pada posisi x, y
        pixel = test.getpixel((x, y))

        # Menampilkan nilai pixel
        print(pixel)

        # Menambah counter
        counter += 1

        # Kondisi untuk berhenti saat jumlah pixel sudah mencapai limit
        if counter >= limit:
            break
    if counter >= limit:
        break
