from PIL import Image
from PIL import ImageEnhance

#menginput gambar dari folder
test = Image.open("harimau-malaya.png")

# menampilkan gambar awal
test.show("Gambar Awal")

# meningkatkan kualitas gambar(Meningkatkan atau menurunkan contrast)
# Meningkatkan Contrast
contrast = 4.0
contrastImage = ImageEnhance.Contrast(test)
ImageNew = contrastImage.enhance(contrast)
ImageNew.show("Contrast + ")

# Menurunkan Contrast
contrast = 0.5
contrastImage = ImageEnhance.Contrast(test)
ImageNew = contrastImage.enhance(contrast)
ImageNew.show("Contrast -")
