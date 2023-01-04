import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pyautogui
import threading
import time



class getScreenShotThread(threading.Thread):
    global screenshots_list

    def run(self):
        # global screenshots_list
        while True:
            img_pyautogui = pyautogui.screenshot()
            # img_pyautogui = cv.cvtColor(np.asarray(img_pyautogui),cv.COLOR_RGB2BGR)
            # img_pyautogui = np.asanyarray(img_pyautogui)
            screenshots_list.append(img_pyautogui)
            time.sleep(5)

class printLengthThread(threading.Thread):
    global screenshots_list

    def run(self):
        while True:
            print(len(screenshots_list))
            time.sleep(4)













if __name__ == "__main__":

    # screenshots_list = []

    # sc_thread = getScreenShotThread()
    # prt_thread = printLengthThread()

    # sc_thread.start()
    # prt_thread.start()

    # time.sleep(200)
    # exit(0)

    # list1 = [1, 2, 3]
    # print(list1)
    # del list1[0]
    # print(list1)

    img = cv.imread("Onmyoji_Automation_Script/pics/01-dual.png")

    pass