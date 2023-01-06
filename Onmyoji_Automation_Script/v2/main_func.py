import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pyautogui
import threading
import time
import random

from button_detection_dual import buttonDetectionDual
from finish_interface_detection import finishInterfaceDetection
from treasure_sign_detection import treasureSignDetection
# from screen_shot import get_screen_shot

class get_screen_shot(threading.Thread):
    # def __init__():
        # super().__init__()



    def run(self):
        global thread_list
        while True:
            rand_pos = random.randint(16, 23)
            print("Random Number: ", rand_pos)
            img = cv.imread("Onmyoji_Automation_Script/testimg/03-t-"+str(rand_pos)+"-1.jpg")
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            for threads in thread_list:
                threads.setImage([rand_pos, img])
            # time.sleep(5)
            t1 = time.time()
            t2 = time.time()

            while (t2 - t1) <= 10.0:
                t2 = time.time()








if __name__ == "__main__":
    
    thread_list = []
    thread1 = buttonDetectionDual()
    thread_list.append(thread1)
    # thread1.start()
    thread2 = finishInterfaceDetection("Onmyoji_Automation_Script/pics/06-T.png")
    thread_list.append(thread2)
    thread3 = finishInterfaceDetection("Onmyoji_Automation_Script/pics/05-T.png")
    thread_list.append(thread3)
    thread4 = treasureSignDetection()
    thread_list.append(thread4)


    for threads in thread_list:
        threads.start()
    

    # time.sleep(3)
    sc_thread = get_screen_shot()
    sc_thread.start()


