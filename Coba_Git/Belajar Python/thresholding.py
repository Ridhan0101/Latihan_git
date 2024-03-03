from PIL import Image


# Menginput Gambar fari folder
test = Image.open('harimau-malaya.png')

# menampilkan Gambar
test.show()

# Function Thresholding
gray = test.convert('L')

threshold = 200
threshold = gray.point(
    lambda x: 255 if x > threshold else 0
)

threshold.show()
