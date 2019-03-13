# encoding=utf-8


import os
import cv2
import config as conf
from utils import game_utils


def exit():
	os.exit()


# default 100
config = {
	'zengsong': {
		'level': 23,
		'img': conf.catch_food_img + os.sep + 'zengsong.png',
		'action': 'click_img',
		'threshold': 0.9,
	},
	'get_food': {
		'level': 22,
		'img': conf.catch_food_img + os.sep + 'get_food.png',
		'action': 'click_img',
		'threshold': 0.9,
	},
	'ok': {
		'level': 21,
		'img': conf.catch_food_img + os.sep + 'ok.png',
		'action': 'do_action_list',
		'action_list': ['click_img', exit],
		'threshold': 0.95,
	},
}

if __name__ == "__main__":
	game_utils.get_curr_status(config, 0.1)
	pass
