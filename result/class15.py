import cv2
import matplotlib.pyplot as plt
import numpy as np

cat_cascade = cv2.CascadeClassifier("res/haarcascade_frontalcatface.xml")

cat = cv2.imread("res/cat2.jpg");
gray = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)

cats = cat_cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in cats:
    cv2.rectangle(cat, (x,y), (x+w,y+h),(20,200,195), 1)

cv2.imshow("Cat", cat)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()