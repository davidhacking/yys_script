# coding=utf-8
import os
import cv2
from PIL import ImageGrab
import numpy as np
import time


def getLoccation(template, threshold, rect=()):
	imgRgb = np.array(ImageGrab.grab(rect).convert('RGB'))
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


if __name__ == '__main__':
	img_dir = r'../img/join_queue'
	icon_index = 0
	threshold = 0.9
	windows_icon = cv2.imread(os.path.join(img_dir, str(icon_index) + '.png'), 0)
	while True:
		time.sleep(0.2)
		loc = getLoccation(windows_icon, threshold)
		c = isHitTarget(loc)
		if not c:
			continue
		top_left = (loc[0]-3, loc[2]-28)
		bottom_right = (top_left[0]+598, top_left[1]+361)
		loc = getLoccation(windows_icon, threshold)

		pass
	pass

