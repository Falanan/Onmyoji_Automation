import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pyautogui
import threading
import time
import random

from button_detection_dual import buttonDetection
# from screen_shot import get_screen_shot

class get_screen_shot(threading.Thread):
    # def __init__():
        # super().__init__()



    def run(self):
        global thread_list
        while True:
            rand_pos = random.randint(20, 23)
            print("Random Number: ", rand_pos)
            img = cv.imread("Onmyoji_Automation_Script/testimg/03-t-"+str(rand_pos)+"-1.jpg")
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            for threads in thread_list:
                threads.setImage(img)
            time.sleep(3)








if __name__ == "__main__":
    
    thread_list = []
    thread1 = buttonDetection()
    thread_list.append(thread1)
    thread1.start()
    # for threads in thread_list:
    #     threads.start()
    
    sc_thread = get_screen_shot()
    sc_thread.start()


    pass

