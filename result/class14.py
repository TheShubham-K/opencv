import cv2
import numpy as np
import matplotlib.pyplot as plt

book  = cv2.imread('res/book.jpg', 0)
scene = cv2.imread('res/scene.jpg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(book, None)
kp2, des2 = orb.detectAndCompute(scene, None)

bruteForce = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

match = bruteForce.match(des1, des2)
match = sorted(match, key = lambda x:x.distance)

matches = cv2.drawMatches(book, kp1, scene, kp2, match, None, flags=2)

plt.imshow(matches)
plt.show()