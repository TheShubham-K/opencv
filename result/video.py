import cv2

cap = cv2.VideoCapture('./res/30_10fps.avi')

fcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
output = cv2.VideoWriter('./result/30_10fps.avi', fcc, 5.0, (400, 200))

# output is responsible to write video
# cv::VideoWrite(destination, codec, frame per second, size of video[w, h])
while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame)
    output.write(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
output.release()
