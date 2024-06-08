import pyautogui
from math import cos, sin, pi
import time


# 先等三秒
time.sleep(3)

# 获取屏幕的分辨率
screen_width, screen_height = pyautogui.size()

# 计算屏幕中央的坐标
center_x = screen_width/2
center_y = screen_height*0.525

# 圆半径
r = 0.4*screen_height

# 边数
N = 112

# 移动鼠标画圆
pyautogui.moveTo(center_x+r, center_y)
pyautogui.mouseDown()
for i in range(N+1):
    angle = 2*pi*i/N
    x = center_x+r*cos(angle)
    y = center_y+r*sin(angle)
    pyautogui.moveTo(x, y)
pyautogui.mouseUp()
# https://matrix67.itch.io/pi-day-challenge?s=35
