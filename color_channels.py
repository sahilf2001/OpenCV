import cv2 as cv
import numpy as np

img = cv.imread('El.jpg')
#cv.imshow('Elon',img)

blank = np.zeros(img.shape[:2],dtype='uint8')


b,g,r = cv.split(img)
# for getting color within it respective color channels
# merging the color channels
blue = cv.merge([b,blank,blank]) # setting all except blue to black
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

#cv.imshow('Blue',b)
#cv.imshow('Green',g)
#cv.imshow('Red',r)

#print(img.shape)
#print(b.shape)
#print(g.shape)
#print(r.shape)

#merging back to the original image
#merged = cv.merge([b,g,r])
#cv.imshow('Merged',merged)


cv.waitKey(0)
cv.destroyAllWindows()