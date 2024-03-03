# import cv2

# # Load the image
# img = cv2.imread('Foto2.jpg')

# # Create a mask for the damaged area
# mask = cv2.imread('Foto1.jpg', 0)

# # Apply the inpainting algorithm
# result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# # Display the result
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# from PIL import Image

# # membaca gambar dari file
# img = Image.open('foto1.jpg')

# # mengubah gambar menjadi grayscale
# gray_img = img.convert('L')

# # mengambil ukuran gambar
# width, height = gray_img.size

# # melakukan thresholding dengan nilai threshold 128
# threshold = 128
# for y in range(height):
#     for x in range(width):
#         if gray_img.getpixel((x, y)) < threshold:
#             gray_img.putpixel((x, y), 0)
#         else:
#             gray_img.putpixel((x, y), 255)

# # menampilkan gambar asli dan gambar yang telah diolah
# img.show()
# gray_img.show()

import numpy as np
import cv2

# Open the image.
img = cv2.imread('cat_damaged.png')

# Load the mask.
mask = cv2.imread('cat_mask.png', 0)

# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Write the output.
cv2.imwrite('Luffy-inpainted.png', dst)

# Display the result
cv2.imshow('Original', img)
cv2.imshow('Result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
