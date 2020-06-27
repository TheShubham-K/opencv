import cv2

cap1 = cv2.VideoCapture('./res/1_30_10fps.avi')
cap2 = cv2.VideoCapture('./res/2_30_10fps.avi')

fcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
output = cv2.VideoWriter('./result/A01.avi', fcc, 10.0,  (400, 200))

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame1", frame1)
    cv2.imshow("Frame2", frame2)
    output.write(frame1)
    output.write(frame2)

    if cv2.waitKey(1) == 27:
        break

cap1.release()
cap2.release()
output.release()
