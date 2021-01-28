import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') #(height,width,shape)
#cv.imshow('Blank',blank)

# 1. Paint the image a certain colour
#blank[:] = 0,255,0 #setting all pixels
#cv.imshow('Green',blank)
# Drawing a square
#blank[200:300,300:400] = 0,0,255
#cv.imshow('Square',blank)
# 2. Draw a rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=3)# thickness=-1 or cv.FILLED means the portion will be filled
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)
# 3. Draw a circle
#cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255),thickness=3)# 40 is radius
#cv.imshow("Circle",blank)
# 4. Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=2)
#cv.imshow("Line",blank)
# 5. Write text
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_DUPLEX,1.0,(121,255,180),thickness=2)
cv.imshow('Text',blank)
#img = cv.imread("El.jpg")
#cv.imshow('Elon',img)

cv.waitKey(0)
cv.destroyAllWindows()
