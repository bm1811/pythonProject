import cv2 as cv
img = cv.imread('josh_duhamel.jpeg')
cv.imshow('Josh', img)

# переведём в серую шкалу
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# заблюрим
blur = cv.GaussianBlur(gray, (7,7) , cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# краевой каскад
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# расширение
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# разъедание
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)


cv.waitKey(0)