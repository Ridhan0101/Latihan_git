import cv2

test = cv2.imread('harimau-malaya.png')
negatif = 255 - test

cv2.imshow('Gambar Awal', test)
cv2.imshow('Gambar Negatif', negatif)


cv2.waitKey()
cv2.destroyAllWindows()
