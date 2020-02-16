import cv2
import numpy as np


def cropimg():
    img = cv2.imread('he.jpg')
    img1 = cv2.imread('he.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 10000, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        x, y, r = circles[0][0]
        r=r+86
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)
        crop = img1[y-r: y+r, x-r : x+r]
        cv2.imwrite('he2.jpg', img)
        cv2.imwrite('cropping.jpg', crop)
        return(crop)
    else :
        print("none")
        return(img)


if __name__ == "__main__":
    cropimg()
