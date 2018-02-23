import pyautogui
import math
import sys

pyautogui.PAUSE = 0.7
px = 921
py = 553

pyautogui.moveTo(px, py, duration=0.1)

while True:
    cx, cy = pyautogui.position()
    dx = cx - px
    dy = cy - py
    d = math.sqrt(dx * dx + dy * dy)
    if d <= 20:
        pyautogui.click(x=px, y=py, button='left')
    else:
        sys.exit(0)
