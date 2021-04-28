import numpy as np
import mss
import mss.tools
import cv2
import time

def screenshot():
    with mss.mss() as sct:
        # Get information of monitor 2
        monitor_number = 1
        mon = sct.monitors[monitor_number]

        # The screen part to capture
        monitor = {
            "top": mon["top"] + 190,  # 100px from the top
            "left": mon["left"] + 160,  # 100px from the left
            "width": 950,
            "height": 640,
            "mon": monitor_number,
        }
        #output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)
        image = np.delete(np.asarray(sct_img),3, 2)

        return image

if __name__ == "__main__":
    cv2.imshow("im", screenshot())
    cv2.waitKey()
    cv2.destroyAllWindows()