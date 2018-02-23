# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
import math
import sys
import _thread

deltaX = 945 - 485
deltaY = 224 - 196
refreshBtnX = 446
refreshBtnY = 588
readyX = 1045
readyY = 524
threshold = 0.9
cwd = os.getcwd()
target = cwd + '/img/rihefang_target.png'
readyTarget = cwd + '/img/ready_target.png'
template = cv2.imread(target, 0)
readyTemplate = cv2.imread(readyTarget, 0)
# width, hight = template.shape[::-1]
tmpPicName = cwd + '/tmp.png'

def distance(px, py):
	cx, cy = pyautogui.position()
	dx = cx - px
	dy = cy - py
	return math.sqrt(dx * dx + dy * dy)

def mouseClick(x, y):
	pyautogui.click(x=x, y=y, button='left')

def grabPic():
	im = ImageGrab.grab()
	im.save(tmpPicName, 'png')
	pass

def isHitTarget(template, threshold):
	t = list(getLoccation(template, threshold))
	return len(t) > 0

def getLoccation(template, threshold):
	imgRgb = np.array(ImageGrab.grab().convert('RGB'))
	imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	return zip(*loc[::-1])

def joinFunc():
	pyautogui.moveTo(refreshBtnX, refreshBtnY, duration=0.1)
	clickX = refreshBtnX
	clickY = refreshBtnY
	while True:
		if distance(refreshBtnX, refreshBtnY) > 20 and distance(clickX, clickY) > 20:
			break
		mouseClick(refreshBtnX, refreshBtnY)
		time.sleep(0.07)
		loc = getLoccation(template, threshold)
		t = list(loc)
		if len(t) <= 0:
			time.sleep(0.1)
			continue
		else:
			clickX = t[0][0] + deltaX
			clickY = t[0][1] + deltaY
			# print("find: ", clickX, clickX)
			mouseClick(clickX, clickY)
			time.sleep(0.1)
			# break

def startFunc():
	while isHitTarget(readyTemplate, threshold) is False:
		time.sleep(2)
	clickTimes = 5
	while clickTimes > 0:
		mouseClick(readyX, readyY)
		clickTimes = clickTimes - 1
		time.sleep(1)
	sys.exit(0)


# try:
_thread.start_new_thread(joinFunc, ())
startFunc()
# except:
# 	print("start thread exception")
# 	pass

