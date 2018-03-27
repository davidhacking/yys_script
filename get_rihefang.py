# -*- coding: utf-8 -*-

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

steps = {
	'zuidui': {
		'x': 225,
		'y': 601,
		'img': cv2.imread(cwd + '/img/zudui.png', 0),
	},
	'all_ready': {
		'img': cv2.imread(cwd + '/img/all_ready.png', 0),
	},
	'yaoqifengyin': {
		'x': 219,
		'y': 555,
		'img': cv2.imread(cwd + '/img/yaoqifengyin.png', 0),
	},
	'yaoqi_result': {
		'img': cv2.imread(cwd + '/img/yaoqi_result.png', 0),
	},
	'tuichu': {
		'img': cv2.imread(cwd + '/img/tuichu.png', 0),
	},
}

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
	while isHitTarget(steps['tuichu']['img'], threshold) is False:
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
	while isHitTarget(steps['all_ready']['img'], threshold) is False:
		time.sleep(0.2)
		mouseClick(readyX, readyY)

def clickZuidui():
	while isHitTarget(steps['zuidui']['img'], threshold) is False:
		time.sleep(1)
	while isHitTarget(steps['yaoqifengyin']['img'], threshold) is False:
		time.sleep(0.2)
		mouseClick(steps['zuidui']['x'], steps['zuidui']['y'])
	pass

def clickYaoqifengyin():
	while isHitTarget(steps['yaoqifengyin']['img'], threshold) is False:
		time.sleep(1)
	while isHitTarget(steps['yaoqi_result']['img'], threshold) is False:
		time.sleep(0.2)
		mouseClick(steps['yaoqifengyin']['x'], steps['yaoqifengyin']['y'])
	pass

def gotoHome():
	while isHitTarget(steps['zuidui']['img'], threshold) is False:
		mouseClick(readyX, readyY)
		time.sleep(1)
	pass

def onKeyboardEvent(event):
	print event.Key

# thread.start_new_thread(joinFunc, ())
# startFunc()

# hm = pyHook.HookManager()
# hm.KeyDown = onKeyboardEvent
# hm.HookKeyboard()

while True:
	clickZuidui()
	clickYaoqifengyin()
	joinFunc()
	startFunc()
	gotoHome()

