import cv2
import numpy as np

img = cv2.imread('res/OpenCV-Logo.jpg', 1)
cv2.imshow("Original Image", img)
w,h, ch = img.shape
black = np.zeros((w,h,ch))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# H_gray = np.float32(H_gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.001, 1)
corners = np.int0(corners)
count = 0

for corner in corners:
    x,y = corner.ravel()
    print(f"({x},{y})")
    count += 1
    cv2.circle(img, (x,y), 5, (255,0,55), -1)
    cv2.circle(black, (x,y), 5, (255,0,55), -1)
    

print(count)
cv2.imshow("H_gray", img)
cv2.imwrite("result/result.jpg", img)
cv2.imshow("Black", black)
cv2.imwrite("result/Black.jpg", black)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()