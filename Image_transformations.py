import cv2 as cv
import numpy as np
img = cv.imread('El.jpg')
#cv.imshow('Elon',img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat,dimensions)

# -x ==> Left
# -y ==> Up
# x  ==> Right
# y ==> Down

translated = translate(img,100,100) #(x,y)
#cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)#assume around centre

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)#scale value default while rotation
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rotated = rotate(img,45) # for clockwise specify negative angle -45
#cv.imshow('Rotated',rotated)

# Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
# 0 ->vertically
# 1 ->horizontal
# -1 -> both vertically and horizontally
flip = cv.flip(img,1)
cv.imshow('Flip',flip)

#Cropping
cropped = img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
cv.destroyAllWindows()

