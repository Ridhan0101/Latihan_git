from PIL import Image


# Menginput Gambar fari folder
test = Image.open('harimau-malaya.png')

#Function Color Transformations
gray = test.convert('L')
gray.show()
Color = test.convert('RGBA')
Color.show()
