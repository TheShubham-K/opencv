import cv2
import numpy as np

dave = cv2.imread("res/roadsigns.jpg", 1)
dave_gray = cv2.cvtColor(dave, cv2.COLOR_BGR2GRAY)

coin = cv2.imread('res/_uTurn.jpg', 0)
w, h = coin.shape[::-1]

res  = cv2.matchTemplate(dave_gray, coin, cv2.TM_CCOEFF_NORMED)
accuracy = 0.35
loc = np.where(res >= accuracy)

for pt in zip(*loc[::-1]):
    cv2.rectangle(dave, pt, (pt[0]+w, pt[1]+h), (155,45,255), 3)

cv2.imshow('Result', dave)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()