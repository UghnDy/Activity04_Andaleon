
import cv2
filePath = 'andy.jpg'
readCvImage = cv2.imread(filePath, 1)
cv2.imshow("This is me, Roland Ivan", readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imread(filePath, 1)

