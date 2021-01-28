import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('El.jpg')
#cv.imshow('ELON',img)

#plt.imshow(img)# here inversion of colors occurs because matplotlib is in RGB format
#plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale',gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#cv.imshow('HSV',hsv)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv_bgr)

# BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
#cv.imshow('L*a*b',lab)

# LAB to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR',lab_bgr)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)# opencv thought we passed in a BGR image thats why the inversion took place

# we can't covert directly from Grayscale to LAB
# but other conversions are possible
plt.imshow(rgb)# we passed RGB image to matplotlib which is its default
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()