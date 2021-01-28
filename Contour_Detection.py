import cv2 as cv
import numpy as np
img = cv.imread('El.jpg')

blank = np.zeros(img.shape,dtype='uint8')
#cv.imshow('Blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)
# instead of canny method
#ret, thresh = cv.threshold(gray,125,125,cv.THRESH_BINARY)# binarise the image if pixel above 125 set to white(255) otherwise set to black(0)
#cv.imshow('Threshold',thresh)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_EXTERNAL --> for getting the external contours
# cv.RETR_TREE --> for getting the hierarchial contours
# cv.RETR_LIST --> for getting all the contours
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),2) #draw the contours on a blank image
# -1 to show all contours
# 2 is the thickness
# 0,0,255 in BGR format
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)
cv.destroyAllWindows()