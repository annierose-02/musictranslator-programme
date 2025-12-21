import cv2 
image = cv2.imread("images/test_image1.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 180 , 255, cv2.THRESH_BINARY)
thresh_mean = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 21 ,9)
cv2.imshow("Adaptive Threshold image",thresh_mean)
cv2.waitKey(0)
#Removes alot of background noise when last parameter inside thresh_mean is larger((9)started with(2))
#When the second to last parameter is larger, the notes and stave lines are darker and more visible((21) started with(11))
