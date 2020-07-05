import cv2
import numpy as np
img = cv2.imread("res/RGB.jpg", 1)

blur = cv2.GaussianBlur(img, (15, 15), sigmaX=1, sigmaY=5)
medianblur = cv2.medianBlur(img, 17)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", blur)
cv2.imshow("Median Blur", medianblur)
# to find a unique code of a key ord() is used.
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()