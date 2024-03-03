from PIL import Image

#Menginput Gambar dari folder
test = Image.open("harimau-malaya.png")

# Menampilkan Gambar Awal
test.show()

#Memotong Gambar perbagian
width, height = test.size

imgCr11 = test.crop((0, 0, width/2, height/2))
imgCr12 = test.crop((width/2, 0, width, height/2))
imgCr21 = test.crop((0, height/2, width/2, height))
imgCr22 = test.crop((width/2, height/2, width, height))

imgCr11.show("Crop 1")
imgCr12.show("Crop 2")
imgCr21.show("Crop 3")
imgCr22.show("Crop 4")
