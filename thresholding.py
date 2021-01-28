#binarisation of am image

import cv2 as cv

img = cv.imread('El.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
#threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)#(thresholding value,max value,type)
#cv.imshow('Simple Threshold',thresh)
#set values between 150 and 255
#threshold, inv_thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)#(thresholding value,max value,type)
#cv.imshow('Simple Inverse Threshold',inv_thresh)
# set values less than 150 and 255

# Adaptive Thresholding-->computer finds the optimal thresholding value
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresholding',adaptive_thresh)




cv.waitKey(0)
cv.destroyAllWindows()