import cv2
import numpy as np

#Load image
image = cv2.imread("images/test_image1.jpg")
if image is None:
    raise FileNotFoundError("Image not found. Please Check file path")

#Convert to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Add Gaussian blur to reduce high-frequency noise
blur = cv2.GaussianBlur(gray_image,(5,5),0)

#Add adaptive thresholding
thresh_mean = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 21 ,13)

#Detecting stavelines
edges = cv2.Canny(thresh_mean, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, rho=1 , theta=1*np.pi/180 , threshold =150, minLineLength=50, maxLineGap=35)

for detectedline in lines:
    x1,y1,x2,y2 = detectedline[0]
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),)

cv2.imshow("Line detected image",image)
cv2.waitKey(0)




















