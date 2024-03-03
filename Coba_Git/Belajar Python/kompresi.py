from PIL import Image

# membaca gambar
img = Image.open('harimau-malaya.png')

# menyimpan gambar dengan kompresi PNG
img.save('gambar_compressed.png', optimize=True)

# membaca gambar yang sudah dikompresi
img_compressed = Image.open('gambar_compressed.png')

# menampilkan informasi gambar
print('Ukuran gambar asli:', img.size)
print('Ukuran gambar terkompresi:', img_compressed.size)
