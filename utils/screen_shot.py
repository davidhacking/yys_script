import os
import cv2
import numpy as np
from PIL import ImageGrab

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


def shot_by_icon(icon, width, height, save_path, delta_x=0, delta_y=0):
	img = cv2.imread(icon, 0)
	loc = getLoccation(img, 0.8)
	d = isHitTarget(loc)
	if not d:
		print "target window not found"
		return False
	shot_img = ImageGrab.grab(bbox=(loc[0][0] + delta_x, loc[0][1] + delta_y,
									loc[0][0] + width + delta_x, loc[0][1] + height + delta_y))
	shot_img.save(save_path)
	return True
	pass


if __name__ == '__main__':
	import os
	import sys
	sys.path.append('../')
	import config
	icon = config.yys_icon
	delta_x = 0
	delta_y = 0
	width = 1280
	height = 720
	import time
	if not os.path.exists(config.screen_shot_path):
		os.makedirs(config.screen_shot_path)
	while True:
		save_path = os.path.join(config.screen_shot_path, '%s.png' % str(time.time()))
		while not shot_by_icon(icon, width, height, save_path, delta_x, delta_y):
			time.sleep(0.1)
		time.sleep(1)
	pass
