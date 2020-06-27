import cv2
import matplotlib.pyplot as plt

img = cv2.imread('res/lena.jpg', 1)
px = img[50,50]
print(px)
# img[100,100] = [0,0,0]
# img[100,300] = [255,255,255]

# img[50:150, 150:200] = [0,0,0]
# img[50:150, 200:250] = [255,255,255]

roi = img[200:400, 200:400]
img[0:200, 0:200] = roi


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()