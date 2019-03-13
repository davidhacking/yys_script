# encoding=utf-8
import os
import cv2
import config as conf
from utils import game_utils



# default 100
config = {
	'tansuo': {
		'img': conf.kun25_img + os.sep + 'tansuo.png',
		'action': 'click_img',
	},
	'tiaozhan': {
		'img': conf.yuhun_img + os.sep + 'tiaozhan.png',
		'action': 'click_img',
	},
	'yuling_btn': {
		'img': conf.yuling_img + os.sep + 'yuling_btn.png',
		'action': 'click_img',
	},
	'yuling_shishen2': {
		'img': conf.yuling_img + os.sep + 'yuling_shishen2.png',
		'action': 'click_img',
	},
	'yuling_shishen3': {
		'img': conf.yuling_img + os.sep + 'yuling_shishen3.png',
		'action': 'click_img',
	},
	'start_game': {
		'level': 19,
		'img': conf.kun25_img + os.sep + 'start_game.png',
		'threshold': 0.95,
		'action': 'click_img',
	},
	'continue_game': {
		'img': conf.kun25_img + os.sep + 'continue_game.png',
		'x': 827,
		'y': 357,
		'range_x': -827 + 900,
		'range_y': -357 + 505,
		'action': 'random_click_with_icon'
	},
}

if __name__ == "__main__":
	game_utils.get_curr_status(config)
	pass
