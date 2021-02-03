import cv2
img = cv2.imread("C:/Users/Sandeep Tukkunor/Desktop/Udemy Notes/Computer-Vision-with-Python/DATA/00-puppy.jpg")

while True:
    cv2.imshow("puppy", img)
    #if we waited atleast one millisecond and pressed thee esc
    if cv2.waitKey(10000):
        break
cv2.destroyAllWindows()