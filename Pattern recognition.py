import cv2
import numpy as np


image_duck = cv2.imread("C:\\Users\\Vincent Chang\\Downloads\\full_duck.jpg", 1)
imageInfo_duck = image_duck.shape
height = imageInfo_duck[0]
width = imageInfo_duck[1]
deep = imageInfo_duck[2]
newInfo = (height, width, deep)
dist = np.zeros(newInfo, np.uint8)

for i in range(0, height):
    for j in range(0, width):
        dist[i, j] = image_duck[i, j]

for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = image_duck[i, j]
        red = int(r)
        blue = int(b)
        green = int(g)
        if (blue > 200 and green > 200 and red > 200):
            dist[i, j] = (0, 0, 255)

cv2.imwrite("C:\\Users\\Vincent Chang\\Desktop\\red_duck.jpg", dist)