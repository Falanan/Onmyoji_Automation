# 22.12.24
 - 完成了同一画面两个按钮识别的理论分析，对于图像识别的理论分析现在还剩下对于outliers的处理。现在的对于outliers的处理思路是data clusting（DBSCAN）
 - Remains: 1. 完善图像识别 2. 获取系统截屏 3.模拟鼠标点击 4.多线程 5.中断

# 22.12.25
- 新增文件：get_screen_shot.ipynb - Test get screenshot function
- New File: get_test_img.ipynb - get new test images(screenshots)
- New Folder: testimg - Add 23*2 images to test the item detection function
- New thinking: Using win32gui and pyautogui can get a sepsific position and area screenshot by getting the thread id then get the screenshot, so actually I do not need to fight with outliers. But this way may has some problems such as it might can be detected by anti cheat system. So, maybe in the future, still need to fight with the outliers.
#### Finished: Get screenshot
- Remains: 1. Improve item detection method(test with new screenshots in testimg folder) 2. Simluate mouse click 3. Multi-thread 4. keybord interruption 5. Pack the "get screenshot" function into a method.

# 12.26
- I think i caught cold today. I feels a little bit unconfortable today. So not that too much progress
- Pack button detection into a class

- Remains: 1. Improve item detection method(test with new screenshots in testimg folder) 2. Simluate mouse click 3. Multi-thread 4. keybord interruption 5. Pack the "get screenshot" function into a method.