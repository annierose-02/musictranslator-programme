import cv2
image = cv2.imread("images/test_image1.jpg")

#Convert to grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray_image)
cv2.waitKey(0)

#Colour is irrelevant, staves and notes are all the exact same shape and position

