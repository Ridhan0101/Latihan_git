import cv2

# Load image
img = cv2.imread('Foto7.jpg', cv2.IMREAD_GRAYSCALE)

# Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

# Display Results
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge Detection', canny)

cv2.waitKey(0)