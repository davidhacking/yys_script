# coding: utf-8

"""
win10 pyHook
install log
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
download pyHook-1.5.1-cp27-cp27m-win_amd64.whl
pip install wheel
pip install pyHook-1.5.1-cp27-cp27m-win_amd64.whl
pywin32 install python 2.7
"""

import pyHook
import pythoncom
import pyautogui
import time
import thread


sleep_time = 0.5
mouse_right_flag = False
mouse_middle_flag = 0


def left_click(event):
	return True


def right_click(event):
	global mouse_right_flag
	if mouse_right_flag:
		mouse_right_flag = False
	else:
		mouse_right_flag = True
	return True


def mouse_event(event):
	global mouse_middle_flag
	global sleep_time
	global mouse_right_flag
	if mouse_right_flag:
		sleep_time = 10
		return True
	mouse_middle_flag += event.Wheel
	if mouse_middle_flag >= 5:
		mouse_middle_flag = 5
	elif mouse_middle_flag <= -5:
		mouse_middle_flag = -5
	sleep_time = 0.5 + (mouse_middle_flag * 0.1)
	print sleep_time
	if sleep_time <= 0.01 and sleep_time >= -0.01:
		sleep_time = 0.1
	return True
	pass


def click_with_f():
	global sleep_time
	while True:
		time.sleep(sleep_time)
		pyautogui.click(pyautogui.position(), button='left')
	pass


if __name__ == "__main__":
	hm = pyHook.HookManager()
	hm.MouseAll = mouse_event
	hm.SubscribeMouseLeftDown(left_click)
	hm.SubscribeMouseRightDown(right_click)
	hm.HookMouse()
	thread.start_new_thread(click_with_f, ())
	pythoncom.PumpMessages()
	print 'end'
	hm.UnhookMouse()
	pass
