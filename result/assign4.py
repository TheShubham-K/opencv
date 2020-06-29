import cv2
import numpy as np

fcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
out = cv2.VideoWriter('./result/assignment_1fps.avi', fcc, 1.0, (400, 200))

red  = np.zeros((200,400,3))
red[75:125,100:300] = [0,0,255]
blue  = np.zeros((200,400,3))
blue[75:125,100:300] = [255,0,0]
green  = np.zeros((200,400,3))
green[75:125,100:300] = [0,255,0]


cv2.imwrite('result/red.jpg',red)
cv2.imwrite('result/blue.jpg',blue)
cv2.imwrite('result/green.jpg',green)

for i in range(1,41):
    red = cv2.imread('result/red.jpg')
    blue = cv2.imread('result/blue.jpg')
    green = cv2.imread('result/green.jpg')
    out.write(red)
    out.write(blue)
    out.write(green)
out.release()
