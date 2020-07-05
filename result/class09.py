import cv2
import numpy as np

img = cv2.imread('res/sudoku.jpg',0)

thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 1)

kernal = np.ones((2,2), np.uint8)

erosion = cv2.erode(thresh, kernal, iterations=1)
dilation = cv2.dilate(thresh, kernal, iterations=1)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernal, iterations=1)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernal, iterations=1)

gradient = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernal, iterations=1)
tophat = cv2.morphologyEx(thresh, cv2.MORPH_TOPHAT, kernal, iterations=1)
blackhat = cv2.morphologyEx(thresh, cv2.MORPH_BLACKHAT, kernal, iterations=1)

cv2.imshow("Image", img)
cv2.imshow("AdaptiveThreshold", thresh)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradient", gradient)
cv2.imshow("TopHat", tophat)
cv2.imshow("BlackHat", blackhat)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()