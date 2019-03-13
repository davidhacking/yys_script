# encoding=utf-8
import os
import cv2
import config as conf
from utils import game_utils



# default 100
config = {
	# 'tansuo': {
	# 	'img': conf.kun25_img + os.sep + 'tansuo.png',
	# 	'action': 'click_img',
	# },
	# 'baqidashe': {
	# 	'img': conf.yuhun_img + os.sep + 'baqidashe.png',
	# 	'action': 'click_img',
	# },
	'jieshou': {
		'img': conf.yuhun_img + os.sep + 'jieshou.png',
		'action': 'click_img',
	},
	'jieshou2': {
        'level': 21,
		'img': conf.yuhun_img + os.sep + 'jieshou2.png',
		'action': 'click_img',
	},
	# 'tiaozhan': {
	# 	'img': conf.yuhun_img + os.sep + 'tiaozhan.png',
	# 	'action': 'click_img',
	# },
	# 'yuhun_btn': {
	# 	'img': conf.yuhun_img + os.sep + 'yuhun_btn.png',
	# 	'action': 'click_img',
	# },
	'start_game': {
		'level': 19,
		'img': conf.kun25_img + os.sep + 'start_game.png',
		'threshold': 0.95,
		'action': 'click_img',
	},
	# 'chuzhanxiaohao': {
	# 	'img': conf.kun25_img + os.sep + 'chuzhanxiaohao.png',
	# 	'level': 30,
	# 	'x': 827,
	# 	'y': 400,
	# 	'range_x': -827 + 900,
	# 	'range_y': -400 + 505,
	# 	'action': 'random_click_with_icon'
	# },
	'continue_game': {
		'img': conf.kun25_img + os.sep + 'continue_game.png',
		'x': 827,
		'y': 457,
		'range_x': -827 + 800,
		'range_y': -457 + 600,
		'action': 'random_click_with_icon'
	},
}

if __name__ == "__main__":
	game_utils.get_curr_status(config)
	pass
