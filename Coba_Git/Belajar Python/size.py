from PIL import Image
from PIL import ImageEnhance


# Menginput Gambar dari folder
test = Image.open("harimau-malaya.png")


print(test.size)
print(test.size[0])  # ukuran horizontal
print(test.size[1])  # ukuran vertical

# test = test.load()

# x = 100
# y = 100

# print(test[x, y])   # nilai RGB dari pixel (x, y)
# print(test[x, y][0])  # nilai R dari pixel (x, y)
# print(test[x, y][1])  # nilai G dari pixel (x, y)
# print(test[x, y][2])  # nilai B dari pixel (x, y)

# menampilkan format file
print(test.format)

#mengetahui mode suatu gambar
print(test.mode)


