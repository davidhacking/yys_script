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
	'25zhang': {
		'img': conf.kun25_img + os.sep + '25zhang.png',
		'action': 'click_img',
		'threshold': 0.95,
	},
	'tansuo_btn': {
		'img': conf.kun25_img + os.sep + 'tansuo_btn.png',
		'action': 'click_img',
	},
	'play_normal12': {
		'level': 24,
		'img': conf.kun25_img + os.sep + 'play_normal2.png',
		'action': 'click_img',
	},
	'play_normal1': {
		'level': 23,
		'img': conf.kun25_img + os.sep + 'play_normal1.png',
		'action': 'click_img',
	},
	'play_boss1': {
		'level': 22,
		'img': conf.kun25_img + os.sep + 'play_boss1.png',
		'action': 'click_img',
	},
	'play_boss2': {
		'level': 21,
		'img': conf.kun25_img + os.sep + 'play_boss2.png',
		'action': 'click_img',
	},
	'start_game': {
		'level': 19,
		'img': conf.kun25_img + os.sep + 'start_game.png',
		'action': 'do_action_list',
		'action_list': [
			{
				'func': 'click_until_img',
				'x': 299,
				'y': 413,
				'range_x': -299 + 492,
				'range_y': -413 + 571,
				'img': conf.kun25_img + os.sep + 'quanbu_btn.png',
			},
			{
				'func': 'click_img_until_img',
				'img': conf.kun25_img + os.sep + 'quanbu_btn.png',
				'threshold': 0.8,
				'until_img': conf.kun25_img + os.sep + 'n_card_btn.png',
				'until_threshold': 0.8,
			},
			{
				'img': conf.kun25_img + os.sep + 'n_card_btn.png',
				'threshold': 0.9,
				'func': 'click_img_until_img',
				'until_img': conf.kun25_img + os.sep + 'huahua.png',
				'until_threshold': 0.8,
			},
			{
				'func': 'random_swipe_with_icon',
				'from_pos': (167, 492),
				'from_range': (-167+221, -492+595),
				'to_pos': (109, 247),
				'to_range': (-109+207, -247+406-100),
			},
			{
				'func': 'random_swipe_with_icon',
				'from_pos': (167+110, 492),
				'from_range': (-167+110+221, -492+595),
				'to_pos': (109+450, 247),
				'to_range': (-109+207, -247+406-100),
			},
			{
				'img': conf.kun25_img + os.sep + 'start_game.png',
				'func': 'click_img',
			},
		]
	},
	'reward': {
		'level': 19,
		'img': conf.kun25_img + os.sep + 'reward.png',
		'threshold': 0.95,
		'action': 'click_img',
	},
	'chuzhanxiaohao': {
		'img': conf.kun25_img + os.sep + 'chuzhanxiaohao.png',
		'level': 21,
		'x': 827,
		'y': 357,
		'range_x': -827 + 1031,
		'range_y': -357 + 505,
		'action': 'random_click_with_icon'
	},
	'continue_game': {
		'img': conf.kun25_img + os.sep + 'continue_game.png',
		'x': 827,
		'y': 357,
		'range_x': -827 + 1031,
		'range_y': -357 + 505,
		'action': 'random_click_with_icon'
	},
}

if __name__ == "__main__":
	game_utils.get_curr_status(config)
	pass
