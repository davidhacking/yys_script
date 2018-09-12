# encoding=utf-8
import os
import cv2
import config as conf
from PIL import ImageGrab
import numpy as np
import time
import random
import pyautogui

pyautogui.FAILSAFE = False

max_times = 50


def random_click_with_icon(icon, x, y, range_x, range_y):
	t = get_location(cv2.imread(icon, 0), 0.6)
	times = 0
	while not is_hit_target(t) and times < max_times:
		times += 1
		print "random_click_with_icon: icon not found"
		time.sleep(0.5)
		t = get_location(cv2.imread(icon, 0), 0.6)
	loc = t[0]
	random_click_top_left((loc[0] + x, loc[1] + y), (range_x, range_y))
	pass


def get_random_pos(top_left, rect):
	click_x = round(random.uniform(top_left[0], top_left[0] + rect[0]), 2)
	click_y = round(random.uniform(top_left[1], top_left[1] + rect[1]), 2)
	return click_x, click_y
	pass


def random_click_top_left(top_left, rect):
	click_x, click_y = get_random_pos(top_left, rect)
	pyautogui.click(x=click_x, y=click_y, button='left')
	pass


def click_img(img, threshold=0.8):
	t = get_location(cv2.imread(img, 0), threshold)
	times = 0
	while not is_hit_target(t) and times < max_times:
		times += 1
		print "click_img: target not found"
		time.sleep(0.5)
		t = get_location(cv2.imread(img, 0), 0.6)
	if times >= max_times:
		return
	loc = t[0]
	shape = read_img_shape(img)
	random_click_top_left(loc, shape)
	pass


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
	kdict_keys = sorted(kdict.items(), key=lambda item: item[1])
	return [k for k, l in kdict_keys]
	pass


def get_location(template, threshold):
	imgRgb = np.array(ImageGrab.grab().convert('RGB'))
	imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)
	res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
	loc = np.where(res >= threshold)
	return zip(*loc[::-1])


def is_hit_target(loc):
	t = list(loc)
	if len(t) > 0:
		return t[0][0], t[0][1]
	else:
		return False


def read_img_shape(img):
	shape = cv2.imread(img, 0).shape
	return (shape[1], shape[0])


def get_curr_status(config):
	config_keys = sort_keys(config)
	print config_keys
	while True:
		for key in config_keys:
			if 'img' not in config[key]:
				continue
			# print "key: ", key
			if 'threshold' not in config[key]:
				t = get_location(cv2.imread(config[key]['img'], 0), 0.8)
			else:
				t = get_location(cv2.imread(config[key]['img'], 0), config[key]['threshold'])
			if is_hit_target(t):
				# return key
				print key
				do_something(config, key)
				pass
			pass
		time.sleep(round(random.uniform(0.05, 0.1), 2))
	pass


def do_action_list(action_list):
	for action in action_list:
		if 'click_until_img' == action['func']:
			click_until_img(conf.yys_icon, action['x'], action['y'], action['range_x'], action['range_y'],
							action['img'])
			pass
		if action['func'] == 'click_img':
			if 'threshold' in action:
				click_img(action['img'], action['threshold'])
			else:
				click_img(action['img'])
		if action['func'] == 'click_img_until_img':
			if 'threshold' in action and 'until_threshold' in action:
				click_img_until_img(action['img'], action['until_img'], action['threshold'], action['until_threshold'])
			elif 'threshold' in action:
				click_img_until_img(action['img'], action['until_img'], action['threshold'])
			elif 'until_threshold' in action:
				click_img_until_img(action['img'], action['until_img'], until_threshold=action['until_threshold'])
		if action['func'] == 'random_swipe_with_icon':
			random_swipe_with_icon(conf.yys_icon, action['from_pos'], action['from_range'], action['to_pos'],
								   action['to_range'])
		pass
	pass


def find_target_num(img, threshold=0.8, next_action=None):
	temp = cv2.imread(img, 0)
	target = get_location(temp, threshold)
	if not target or type(target) != list or len(target) <= 0:
		return None
	target_num = len(target)
	print "find_target_num: ", target_num
	if not next_action:
		return None
	target_num = str(target_num)
	if target_num in next_action:
		return next_action[target_num]
	else:
		return next_action['default']
	pass


def do_action_obj(action_obj, id='init'):
	def ret_next(action, next_action):
		if 'next' in action:
			return action['next']
		return next_action if next_action else 'finish'
		pass

	def _do_action(action):
		next_action = 'finish'
		if not action:
			return next_action
		if 'click_until_img' == action['func']:
			next_action = click_until_img(conf.yys_icon, action['x'], action['y'], action['range_x'], action['range_y'],
										  action['img'])
			pass
		elif action['func'] == 'click_img':
			if 'threshold' in action:
				next_action = click_img(action['img'], action['threshold'])
			else:
				next_action = click_img(action['img'])
		elif action['func'] == 'click_img_until_img':
			if 'threshold' in action and 'until_threshold' in action:
				next_action = click_img_until_img(action['img'], action['until_img'], action['threshold'],
												  action['until_threshold'])
			elif 'threshold' in action:
				next_action = click_img_until_img(action['img'], action['until_img'], action['threshold'])
			elif 'until_threshold' in action:
				next_action = click_img_until_img(action['img'], action['until_img'],
												  until_threshold=action['until_threshold'])
		elif action['func'] == 'random_swipe_with_icon':
			next_action = random_swipe_with_icon(conf.yys_icon, action['from_pos'], action['from_range'],
												 action['to_pos'],
												 action['to_range'])
		elif 'find_target_num' == action['func']:
			next_action = find_target_num(action['img'], action['threshold'], action['next_action'])
		return ret_next(action, next_action)
		pass

	while id != 'finish':
		id = _do_action(action_obj.get(id, None))
	pass


def do_something(config, key):
	# default random click
	if config[key]['action'] == 'click_img':
		if 'click_img_param' not in config[key]:
			if 'threshold' in config[key]:
				click_img(config[key]['img'], config[key]['threshold'])
			else:
				click_img(config[key]['img'])
		else:
			if 'threshold' in config[key]:
				click_img(config[key]['click_img_param'], config[key]['threshold'])
			else:
				click_img(config[key]['click_img_param'])
	if config[key]['action'] == 'random_click_with_icon':
		random_click_with_icon(conf.yys_icon, config[key]['x'], config[key]['y'],
							   config[key]['range_x'], config[key]['range_y'])
	if config[key]['action'] == 'do_action_list':
		do_action_list(config[key]['action_list'])
		pass
	if config[key]['action'] == 'do_action_obj':
		do_action_obj(config[key]['action_obj'])
		pass
	pass


def click_until_img(icon, x, y, range_x, range_y, img):
	temp = cv2.imread(img, 0)
	times = 0
	while not is_hit_target(get_location(temp, 0.8)) and times < max_times:
		times += 1
		random_click_with_icon(icon, x, y, range_x, range_y)
		time.sleep(0.5)
	pass


def click_img_until_img(img, until_img, threshold=0.8, until_threshold=0.8):
	temp = cv2.imread(until_img, 0)
	times = 0
	while not is_hit_target(get_location(temp, threshold)) and times < max_times:
		times += 1
		click_img(img, until_threshold)
		time.sleep(0.5)
	time.sleep(1)
	pass


def random_swipe_with_icon(icon, from_pos, from_range, to_pos, to_range):
	t = get_location(cv2.imread(icon, 0), 0.6)
	times = 0
	while not is_hit_target(t) and times < max_times:
		times += 1
		print "random_click_with_icon: icon not found"
		time.sleep(0.5)
		t = get_location(cv2.imread(icon, 0), 0.6)
	loc = t[0]
	pos1_x, pos1_y = get_random_pos((from_pos[0] + loc[0], from_pos[1] + loc[1]), from_range)
	pos2_x, pos2_y = get_random_pos((to_pos[0] + loc[0], to_pos[1] + loc[1]), to_range)
	swipe((pos1_x, pos1_y), (pos2_x, pos2_y))
	time.sleep(1)
	pass


def swipe(pos1, pos2):
	print "swipe: ", pos1, pos2
	pyautogui.moveTo(pos1[0], pos1[1])
	pyautogui.dragTo(pos2[0], pos2[1], 0.5, button='left')
	pass


if __name__ == "__main__":
	pass
