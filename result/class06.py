import cv2


img = cv2.imread('res/threshold.jpg',0)
bkpg = cv2.imread('res/bookpage.jpg',0)

# simple t 127, p<127, p->0, p->127,  p->M m ->max value -> 255 
# res, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# res, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# res, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# res, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# res, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

thresh6 = cv2.adaptiveThreshold(bkpg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)
thresh7 = cv2.adaptiveThreshold(bkpg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)

cv2.imshow('Original Image', bkpg)
# cv2.imshow('Original Image', img)
# cv2.imshow('THRESH_BINARY', thresh1)
# cv2.imshow('THRESH_BINARY_INV', thresh2)
# cv2.imshow('THRESH_TOZERO', thresh3)
# cv2.imshow('THRESH_TOZERO_INV', thresh4)
# cv2.imshow('THRESH_TOZERO_INV', thresh5)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C', thresh6)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C', thresh7)

cv2.imwrite('result/ADAPTIVE_THRESH_MEAN_C.jpg', thresh6)
cv2.imwrite('result/ADAPTIVE_THRESH_GAUSSIAN_C.jpg', thresh7)


cv2.waitKey(0)
cv2.destroyAllWindows()