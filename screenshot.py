import numpy as np
import mss
import mss.tools
import cv2
import time

def find():
    targ = cv2.imread('topright.png')
    with mss.mss() as sct:
        sct = sct.grab(sct.monitors[1])
        img = np.delete(np.asarray(sct),3, 2)
    res = cv2.matchTemplate(targ, img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left=max_loc

    return top_left

def screenshot(top_left):
    #with mss.mss(display=":0.0") as sct:
    with mss.mss() as sct:
        # The screen part to capture
        #output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(sct.monitors[1])
        image = np.delete(np.asarray(sct_img),3, 2)

        image = image[top_left[1]:top_left[1]+630,top_left[0]:top_left[0]+950]

        return image

if __name__ == "__main__":
    top_left = find()
    time.sleep(1)
    cv2.imshow("im", screenshot(top_left))
    cv2.waitKey()
    cv2.destroyAllWindows()