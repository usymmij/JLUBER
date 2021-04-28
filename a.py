import numpy as np
import cv2

n = cv2.imread("noice.jpg")
n2 = cv2.imread("noice2.jpg")
cv2.imshow("sada", n)
cv2.imshow("dsnj", n2)
cv2.waitKey(0)
print(np.array_equal(n[100,850],[255,255,25]))
print(np.array_equal(n2[100,850],[255,255,25]))