import cv2 as cv

img = cv.imread('El.jpg')

# kernel is a window we draw over a specific portion of the image

# 1.Averaging
average = cv.blur(img,(7,7)) #(3,3) is the kernel size
cv.imshow('Average Blur',average)
# 2.Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)# 0 is the weight value
cv.imshow('Gaussian Blur',gauss)
# 3.Median Blur --> for removing noise effectively
median = cv.medianBlur(img,7) # assume it to be 7x7
cv.imshow('Median Blur',median)
# 4.Bilateral Blur -->applies blurring without removing edges
bilateral = cv.bilateralFilter(img,5,15,15)
#(d,sigmaColor,sigmaSpace)
# d--> Diameter of each pixel in the neighbourhood
# sigmaColor --> Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together, resulting in larger areas of semi-equal color.
# sigmaSpace --> Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough. When d>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace.
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)
cv.destroyAllWindows()