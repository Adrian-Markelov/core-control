import cv2
img = cv2.imread('data/shallow_normal.jpg')

#print(type(img))
#print(img.shape)


img = img[1500:3500,:,:]

cv2.imshow("hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
