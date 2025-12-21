import cv2
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
cv2.imshow("Threshold blur", thresh_mean)
cv2.waitKey(0)



















