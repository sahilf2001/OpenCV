import cv2

img = cv2.imread("El.jpg")
#cv2.imshow("Elon",img)

# Converting to gray scale image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)

# Blur
blur = cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT) #(7,7) kernel size
#cv2.imshow('Blur',blur)

# Edge Cascade
canny = cv2.Canny(img,125,175) # threshold values
#cv2.imshow('Canny Edge',canny)

# Dilating the image
dilated = cv2.erode(canny,(7,7),iterations=3)
#cv2.imshow('Dilated',dilated)

# Eroding the image
eroded = cv2.erode(dilated,(3,3),iterations=1)
#cv2.imshow('Eroded',eroded)

# Resize
resized = cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA) #interpolation useful when shrinking below original size
# these can be used to scale the image to larger sizes
#cv2.INTER_LINEAR
#cv2.INTER_CUBIC
cv2.imshow('Resized',resized)

#Cropping
cropped = img[50:200,200:400]
cv2.imshow('Cropped',cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()