from PIL import Image
from PIL import ImageFilter

# Menginput Gambar dari folder
test = Image.open("Luffy.jpg")

# membuat edge (Garis Tepi)
Edge = test.convert("L")
Edge = Edge.filter(ImageFilter.FIND_EDGES)
Edge.show()
