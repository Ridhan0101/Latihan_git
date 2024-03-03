import cv2

# Load image
img = cv2.imread('Foto6.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel Edge Detection
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display Results
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Edge Detection', sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()