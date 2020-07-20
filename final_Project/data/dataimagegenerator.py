import os
import cv2
import imutils

imagePath = "./images/"

imageAddress = os.listdir(imagePath)

count = 755
imageCount = 1
# this is for images till 999
# for image in imageAddress:
#   address = imagePath + image
#   img = cv2.imread(address)
#   address = "with_mask/" + str(count) + "-with-mask.jpg"
#   cv2.imwrite(address, img)
#   count += 1
#   imageCount += 1
#   if imageCount == 1162:
#     break

for image in imageAddress:
  if imageCount >= 1162:
    address = imagePath + image
    img = cv2.imread(address)
    address = "with_mask/augmented_image_" + str(count) + ".jpg"
    cv2.imwrite(address, img)
    count += 1
    imgFlip = cv2.flip(img, 0)
    address = "with_mask/augmented_image_" + str(count) + ".jpg"
    cv2.imwrite(address, img)
    count += 1
    img45 = imutils.rotate(img, 45)
    address = "with_mask/augmented_image_" + str(count) + ".jpg"
    cv2.imwrite(address, img45)
    count += 1
    img20 = imutils.rotate(img, -20)
    address = "with_mask/augmented_image_" + str(count) + ".jpg"
    cv2.imwrite(address, img20)
    count += 1
  imageCount += 1