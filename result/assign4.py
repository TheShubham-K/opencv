import cv2
import numpy as np

cap = cv2.VideoCapture('./result/assign4_1fps.avi')
red  = np.zeros((500,600,3))
blue  = np.zeros((500,600,3))
green  = np.zeros((500,600,3))

red = cv2.rectangle(red, (50,50),(350,150), (0,0,255),5)
green = cv2.rectangle(green, (50,50),(350,150), (0,255,0),5)
blue = cv2.rectangle(blue, (50,50),(350,150), (255,0,0),5)

fcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
out = cv2.VideoWriter('./result/assign4_1fps.avi', fcc, 5.0, (400, 200))

while True:
    count = 40
    
    while count>0:
        ret, frame = cap.read()
        cv2.imshow("Frame", frame)
        out.write(red)
        ret, frame = cap.read()
        cv2.imshow("Frame", blue)
        out.write(blue)
        ret, frame = cap.read()
        cv2.imshow("Frame", green)
        out.write(green)
        count -= 1
    
    if cv2.waitKey(1) == 27:
        break

out.release()