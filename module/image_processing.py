import numpy as np
from matplotlib import pyplot as plt
import cv2

def grayImg(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
def bilateralFilterImg(img):
    gray = grayImg(img)
    blurred = cv2.bilateralFilter(gray,10,50,50)
    return blurred
def HoughCirclesImg(img):
    """HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles"""
    minDist = 100
    param1 = 30 #500
    param2 = 20 #200 #smaller value-> more false circles
    minRadius = 5
    maxRadius = 200 #10
    blurred = bilateralFilterImg(img)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.uint16(np.around(circles))
    if len(circles[0]) == 1:
        x, y, r = circles[0][0]
    return x-r, y+r, x+r, y-r
def cropImage(img:np.ndarray, x1:int, y1:int, x2:int, y2:int)->np.ndarray:
    """
    Interference Image
    """
    # Resize the overlay image to match the region size
    roi = img.copy()[y1:y2, x1:x2]
    # Create a black overlay image with reduced opacity
    overlay = np.zeros_like(img)
    overlay[y1:y2, x1:x2] = [0, 0, 0]  # Black color
    # Blend the overlay image onto the original image
    alpha = 0.7  # Opacity factor
    darkened_image = cv2.addWeighted(img, 1 - alpha, overlay, alpha, 0)
    # Replace the region in the original image with the blended image
    darkened_image[y1:y2, x1:x2] = img[y1:y2, x1:x2]
    return darkened_image, img[y1:y2, x1:x2]
if __name__ == "__main__":
    img = cv2.imread('image/11.JPG', 1)
    x1, y1, x2, y2 = HoughCirclesImg(img)
    darkened_image, _ = cropImage(img, x1, y1, x2, y2)
    plt.subplot(121),plt.imshow(bilateralFilterImg(img)),plt.title('bilateralFilter')
    # plt.subplot(132),plt.imshow(circleImg),plt.title("circleImg")
    plt.subplot(122),plt.imshow(darkened_image),plt.title("darkened_image")
    plt.xticks([]), plt.yticks([])
    plt.show()