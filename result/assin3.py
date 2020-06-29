import cv2
import numpy as np

fcc=cv2.VideoWriter_fourcc('X','V','I','D')
out=cv2.VideoWriter('result/assignment03.avi',fcc,15.0,(400,200))

red=np.zeros((200,400,4))
red = cv2.rectangle(red, (50,50),(125,125), (0,0,255),15)

orange=np.zeros((200,400,4))
orange = cv2.rectangle(orange, (85,85),(150,150), (255,140,0),15)

blue=np.zeros((200,400,4))
blue = cv2.rectangle(blue, (75,75),(125,125), (255,0,0),15)

green=np.zeros((200,400,4))
green = cv2.rectangle(green, (150,150),(200,200), (0,255,0),15)

cv2.imwrite("result/r.jpg",red)
cv2.imwrite("result/b.jpg",blue)
cv2.imwrite("result/g.jpg",green)
cv2.imwrite("result/o.jpg",orange)

for i in range(1,51):
    red=cv2.imread("result/r.jpg")
    blue=cv2.imread("result/b.jpg")
    green=cv2.imread("result/g.jpg")
    orange=cv2.imread("result/o.jpg")
    out.write(red)
    out.write(green)
    out.write(blue)
    out.write(orange)
out.release()