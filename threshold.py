import cv2 
image = cv2.imread("images/test_image1.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 127 , 255, cv2.THRESH_BINARY)
cv2.imshow("Binary image" ,binary_image)
cv2.waitKey(0)
#No background noise, howeve stave lines and notes are less clearer than threshold 2 but better since background noise is not an issue