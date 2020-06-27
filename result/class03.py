import cv2
import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((500, 650, 3))


img = cv2.line(img, (520, 250), (150, 250), (255, 115, 5), 5)
img = cv2.rectangle(img, (30, 220), (120, 270), (255, 0, 5), -1)
img = cv2.circle(img, (590, 250), 55, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
string = "Shubham Kumar"
img = cv2.putText(img, string, (175, 450), font, 1.5, (255, 0, 0), 1)
pts = np.array([[0, 0], [650, 495], [0, 495], [650, 0]], np.int32)
img = cv2.polylines(img, [pts], True, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()
