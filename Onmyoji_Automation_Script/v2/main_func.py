import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pyautogui
import threading
import time
import random
import win32gui
import mouse
import pymouse

from button_detection_dual import buttonDetectionDual
from finish_interface_detection import finishInterfaceDetection
from treasure_sign_detection import treasureSignDetection
# from screen_shot import get_screen_shot

class get_screen_shot_test(threading.Thread):
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
                threads.setImage([[0, 0], img])
            time.sleep(5)
            # t1 = time.time()
            # t2 = time.time()

            # while (t2 - t1) <= 10.0:
            #     t2 = time.time()



class getScreenShot(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(getScreenShot, self).__init__(*args, *kwargs)
        self.hwnd_title = dict() # Save thread name and window name

        self.task_list = []
        
        
        # win32gui.EnumWindows(get_all_hwnd, 0)
        # for pid in self.hwnd_title.keys():
        #     print(pid)
        #     if "任务管理器" in self.hwnd_title[pid]:
        #         # print(pid)
        #         self.task_list.append(pid)



    def get_all_hwnd(self, hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            self.hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    def run(self):
        global thread_list
        
        win32gui.EnumWindows(self.get_all_hwnd, 0)
        for pid in self.hwnd_title.keys():
            # print(pid)
            if "阴阳师" in self.hwnd_title[pid]:
                # print(pid)
                self.task_list.append(pid)

        while True:
            for pid in self.task_list:
                # print(pid)
                bbox = win32gui.GetWindowRect(pid)
                bbox = list(bbox)
                bbox[2] = bbox[2] - bbox[0]
                bbox[3] = bbox[3] - bbox[1]
                # print("Client position:",bbox)
                screenshot = pyautogui.screenshot(region=bbox)
                screenshot = np.asarray(screenshot)
                # plt.imshow(screenshot)
                # plt.show()
                pos = [bbox[0], bbox[1]]
                for thread in thread_list:
                    thread.setImage([pos, screenshot])
                time.sleep(0.2)
            time.sleep(6)
                    




class mouseClick(threading.Thread):
    # global click_list
    def __init__(self, *args, **kwargs):
        super(mouseClick, self).__init__(*args, *kwargs)
        self.click_list = []
        self.m = pymouse.PyMouse()

    def setPosition(self, bbox):
        global click_list
        click_list.append(bbox)

    def run(self):
        global click_list
        # while True:
        #     if len(click_list) != 0:
        #         print("Click Position:", click_list[0])
        #         del click_list[0]
        while True:
            if len(click_list) != 0:
                click_pos = click_list[0]
                mouse.move(click_pos[0], click_pos[1] , absolute=True, duration=0.1)
                time.sleep(0.2)
                # mouse.click("right")
                self.m.click(click_pos[0], click_pos[1])
                del click_list[0]
                # time.sleep(0.2)










if __name__ == "__main__":
    
    thread_list = []

    click_list = []

    mouse_thread = mouseClick()
    mouse_thread.start()
    sc_thread = getScreenShot()
    sc_thread.start()

    button_thread = buttonDetectionDual(click_list)
    thread_list.append(button_thread)
    # finish_interface_thread = finishInterfaceDetection("Onmyoji_Automation_Script/pics/06-T.png", click_list)
    # thread_list.append(finish_interface_thread)
    # finish_interface2_thread = finishInterfaceDetection("Onmyoji_Automation_Script/pics/05-T.png", click_list)
    # thread_list.append(finish_interface2_thread)
    # treasure_thread = treasureSignDetection(click_list)
    # thread_list.append(treasure_thread)


    for threads in thread_list:
        threads.start()
    

    # time.sleep(3)
    # sc_thread = get_screen_shot()
    # sc_thread = getScreenShot()
    # sc_thread.start()

    # time.sleep(20)
    # exit(0)


