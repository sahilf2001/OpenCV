import cv2

img = cv2.imread("El.jpg")
cv2.imshow("Elon Musk",img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

resized = rescaleFrame(img)
cv2.imshow('Resized',resized)

'''
def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()


