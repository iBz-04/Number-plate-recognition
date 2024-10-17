# PACKAGES NEEDED
import cv2
from matplotlib import pyplot as plt
import numpy as np
import easyocr
import imutils
import random

# IMAGE PROCESSING

# reading the image
img = cv2.imread("testMain.jpg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
# plt.show()

# converting image to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# noise reductions
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
# displaying processed image
plt.imshow(cv2.cvtColor(bfilter, cv2.COLOR_BGR2RGB))
plt.title('Processed Image')
# plt.show()

# EDGE DETECTION
# Using the canny edge detection algorithm -
# smoothening the photo and scanning for areas where brightness changes sharply
edged = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
# plt.show()

# FINDING CONTOURS
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# loop over contours to find best possible contour of 10 contours
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
# output is the coordinates of the number plate
print("location: ", location)

# MASKING OUT NUMBER PLATE AREA
# blank image with same dimensions as original image
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask,[location],0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()


