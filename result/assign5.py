import cv2
import numpy as np

img = cv2.imread('res/bookpage.jpg',0)


thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 3)

kernal = np.ones((2,2), np.uint8)


opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernal, iterations=1)
# cv2.imshow('Original Image', img)

cv2.imshow('thresh',thresh)

cv2.imshow('Result',opening)

# cv2.imwrite('result/aSSIGN_05.jpg',opening)

if cv2.waitKey(0)== 27:
    cv2.destroyAllWindows()