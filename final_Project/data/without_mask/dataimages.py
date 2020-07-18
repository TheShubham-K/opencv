# import os
# import cv2

# imagePath = "./images/"

# imageAddress = os.listdir(imagePath)

# count = 755
# for i in range(1, 1162):

import tensorflow_datasets as tfds

ds = tfds.load('celeb_a', split='train')
for ex in ds.take(4):
  print(ex)