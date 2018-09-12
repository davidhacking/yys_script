# encoding=utf-8
import os
import cv2
import config as conf
from PIL import ImageGrab
import numpy as np
import time
import random
import pyautogui


def random_click_with_icon(icon, x, y, range_x, range_y):
	t = getLoccation(cv2.imread(icon, 0), 0.6)
	if isHitTarget(t):
		loc = t[0]
		random_click_top_left((loc[0] + x, loc[1] + y), (range_x, range_y))
		pass
	else:
		print "click_img: target not found"
		pass
	pass


def random_click_top_left(top_left, rect):
	click_x = round(random.uniform(top_left[0], top_left[0] + rect[0]), 2)
	click_y = round(random.uniform(top_left[1], top_left[1] + rect[1]), 2)
	pyautogui.click(x=click_x, y=click_y, button='left')
	pass


def click_img(img):
	t = getLoccation(cv2.imread(img, 0), 0.6)
	if isHitTarget(t):
		loc = t[0]
		shape = read_img_shape(img)
		random_click_top_left(loc, shape)
		pass
	else:
		print "click_img: target not found"
		pass
	pass


# default 100
config = {
	'tingzhong': {
		'img': conf.bgye_img + os.sep + 'tingzhong.png',
		'action': 'click_img',
	},
	'denglong': {
		'img': conf.bgye_img + os.sep + 'denglong.png',
		'action': 'click_img',
	},
	'jinru': {
		'img': conf.bgye_img + os.sep + 'jinru.png',
		'action': 'click_img',
	},
	'qiyueshu': {
		'img': conf.bgye_img + os.sep + 'qiyueshu.png',
		'action': 'click_img',
	},
	'choose': {
		'img': conf.bgye_img + os.sep + 'choose.png',
		'level': 5,
		'x': 535,
		'y': 390,
		'range_x': -535 + 592,
		'range_y': -390 + 481,
		'action': 'random_click_with_icon'
	},
	'ya': {
		'img': conf.bgye_img + os.sep + 'ya.png',
		'click_img_param': conf.bgye_img + os.sep + 'kaishi.png',
		'level': 4,
		'action': 'click_img'
	},
	'playing': {
		'img': conf.bgye_img + os.sep + 'playing.png',
		'level': 3,
		'x': 143,
		'y': 357,
		'range_x': -143 + 973,
		'range_y': -357 + 505,
		'action': 'random_click_with_icon'
	}
}


def sort_keys(conf):
	kdict = {}
	for key in conf.keys():
		level = 100
		if 'level' in conf[key]:
			if conf[key] < 0:
				continue
			level = conf[key]['level']
		kdict[key] = level
		pass
	sorted(kdict.items(), key=lambda item: item[1])
	return kdict.keys()
	pass


config_keys = sort_keys(config)


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


def read_img_shape(img):
	shape = cv2.imread(img, 0).shape
	return (shape[1], shape[0])
	pass


def get_curr_status():
	while True:
		for key in config_keys:
			if 'img' not in config[key]:
				continue
			t = getLoccation(cv2.imread(config[key]['img'], 0), 0.6)
			if isHitTarget(t):
				# return key
				print key
				do_something(key)
				pass
			pass
		time.sleep(round(random.uniform(0.05, 0.1), 2))
	pass


def do_something(key):
	# default random click
	if config[key]['action'] == 'click_img':
		if 'click_img_param' not in config[key]:
			click_img(config[key]['img'])
		else:
			click_img(config[key]['click_img_param'])
	if config[key]['action'] == 'random_click_with_icon':
		random_click_with_icon(conf.yys_icon, config[key]['x'], config[key]['y'],
								config[key]['range_x'], config[key]['range_y'])
	pass


def main():

	pass


if __name__ == "__main__":
	# print read_img_shape(config['tingzhong']['img'])
	get_curr_status()
	pass
