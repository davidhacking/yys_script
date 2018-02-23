import os
"""
https://github.com/juxiangwu/tensorflow-learning
"""
def mathc_img(image, target, threshold):
	import cv2
	import numpy as np
	img_rgb = cv2.imread(image)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	# assert none
	template = cv2.imread(target,0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	print res
	loc = np.where(res >= threshold)
	print loc
	print zip(*loc[::-1])
	for pt in zip(*loc[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
	cv2.imshow('Detected',img_rgb)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

cwd = os.getcwd()
image = cwd + "/img/rihefang_ex.png"
target = cwd + '/img/rihefang_target.png'
mathc_img(image, target, 0.9)