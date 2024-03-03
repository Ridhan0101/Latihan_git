from PIL import Image


# Menginput Gambar dari Folder
test = Image.open("harimau-malaya.png")
# Membaca Nilai Pixel
# lebar, tinggi = test.size
# for i in range(lebar):
#     for j in range(tinggi):
#         nilai_piksel = test.getpixel((i, j))
#         print(nilai_piksel)

# menampilkan gambar awal
test.show("Gambar Awal")

# merubah ke grayscale
gray = test.convert('L')

gray.show("Grayscale")

