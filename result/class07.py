import cv2
import numpy as np

astro = cv2.imread('res/astro.jpg', 1)
sea  = cv2.imread('res/sea.jpg', 1)
# cv2.imshow('Astro', astro)
# cv2.imshow('Sea', sea)

hsv = cv2.cvtColor(astro, cv2.COLOR_BGR2HSV)
lower_green = np.array([50,150,180])
upper_green = np.array([200,245,255])

msk = cv2.inRange(hsv, lower_green, upper_green)
msk_inv = cv2.bitwise_not(msk)
astro = cv2.bitwise_and(astro, astro, mask=msk_inv)
sea = cv2.bitwise_and(sea, sea, mask=msk)
result = cv2.add(astro, sea)

# cv2.imshow("Background", sea)
# cv2.imshow("Mask", msk)
# cv2.imshow("Mask_Inverse", msk_inv)
# cv2.imshow("HSV Image", hsv)
cv2.imshow("Result", result)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()