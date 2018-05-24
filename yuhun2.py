import os
import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
import math
import sys
import thread
# import pythoncom
# import pyHook
import time
import random

pyautogui.PAUSE = 0.7
px = 846
py = 474
cwd = os.getcwd()

# pyautogui.moveTo(px, py, duration=0.1)

# while True:
#     cx, cy = pyautogui.position()
#     dx = cx - px
#     dy = cy - py
#     d = math.sqrt(dx * dx + dy * dy)
#     if d <= 20:
#         pyautogui.click(x=px, y=py, button='left')
#     else:
#         sys.exit(0)


def getLoccation(template, threshold):
	imgRgb = np.array(ImageGrab.grab().convert('RGB'))
	imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	return zip(*loc[::-1])

def isHitTarget(loc):
	t = list(loc)
	if len(t) > 0:
		return t[0][0], t[0][1]
	else:
		return False

obj = {
	'yys_icon': {
		'img': cv2.imread(cwd + '/img/yys_icon.png', 0)
	},
	'challenge_btn': {
		'img': cv2.imread(cwd + '/img/challenge_btn.png', 0)
	},
	'qingming': {
		'img': cv2.imread(cwd + '/img/qingming.png', 0)
	},
	'overcome': {
		'img': cv2.imread(cwd + '/img/overcome.png', 0)
	},
}
threshold = 0.9
# distance from challenge button to yys icon 845 472
repeat_click_flag = False
while True:
	time.sleep(0.5)
	loc = getLoccation(obj['yys_icon']['img'], threshold)
	c = isHitTarget(loc)
	if c:
		pyautogui.moveTo(c[0] + random.randint(0, 500), c[1] + random.randint(0, 500))
		loc = getLoccation(obj['challenge_btn']['img'], 0.6)
		d = isHitTarget(loc)
		if d == False:
			loc = getLoccation(obj['overcome']['img'], 0.6)
			e = isHitTarget(loc)
			print "find overcome: ", e
			if e:
				repeat_click_flag = True
			if repeat_click_flag:
				pyautogui.click(x=e[0] - random.randint(0, 100), y=e[1] - random.randint(0, 100), button='left')
		else:
			pyautogui.click(x=d[0] + random.randint(0, 70), y=d[1] + random.randint(0, 30), button='left')
			repeat_click_flag = False