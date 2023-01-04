import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import pyautogui
import threading
import math
import time
import random


class get_screen_shot(threading.Thread):
    # def __init__():
        # super().__init__()



    def run(self):
        global thread_list
        while True:
            rand_pos = random.randint(1, 23)
            img = cv.imread("testimg/03-t-"+str(rand_pos)+"-0.jpg")
            for threads in thread_list:
                threads.setImage(img)