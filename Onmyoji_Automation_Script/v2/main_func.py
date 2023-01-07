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
            time.sleep(5)
            # t1 = time.time()
            # t2 = time.time()

            # while (t2 - t1) <= 10.0:
            #     t2 = time.time()

class mouseClick(threading.Thread):
    # global click_list
    def __init__(self, *args, **kwargs):
        super(mouseClick, self).__init__(*args, *kwargs)
        self.click_list = []

    def setPosition(self, bbox):
        global click_list
        click_list.append(bbox)

    def run(self):
        global click_list
        while True:
            if len(click_list) != 0:
                print("Click Position:", click_list[0])
                del click_list[0]


    pass







if __name__ == "__main__":
    
    thread_list = []

    click_list = []

    mouse_thread = mouseClick()
    mouse_thread.start()

    button_thread = buttonDetectionDual(click_list)
    thread_list.append(button_thread)
    finish_interface_thread = finishInterfaceDetection("Onmyoji_Automation_Script/pics/06-T.png", click_list)
    thread_list.append(finish_interface_thread)
    finish_interface2_thread = finishInterfaceDetection("Onmyoji_Automation_Script/pics/05-T.png", click_list)
    thread_list.append(finish_interface2_thread)
    treasure_thread = treasureSignDetection(click_list)
    thread_list.append(treasure_thread)


    for threads in thread_list:
        threads.start()
    

    # time.sleep(3)
    sc_thread = get_screen_shot()
    sc_thread.start()


