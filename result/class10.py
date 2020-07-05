import cv2
import numpy as np

img = cv2.imread('res/bookpage.jpg')



# sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
# sobelXY = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)
# kernal = np.ones((2,2), np.uint8)
# laplacian_inv = cv2.bitwise_not(laplacian)
# closing = cv2.morphologyEx(laplacian_inv, cv2.MORPH_CLOSE, kernal, iterations=1)


cv2.imshow("Deer", img)
# cv2.imshow("SobelX", sobelX)
# cv2.imshow("SobelY", sobelY)
# cv2.imshow("SobelXY", sobelXY)
cv2.imshow("Laplacian", laplacian)
# cv2.imshow("Closing", closing)




if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()