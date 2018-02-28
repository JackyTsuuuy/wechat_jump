from PIL import Image
from subprocess import Popen
import pyautogui
import math
import time
import os

X_start = 0
Y_start = 0

X_end = 0
Y_end = 0

while True:

	#截屏adb
	Popen('./adb.exe shell /system/bin/screencap -p /sdcard/tyt/screenshot.png')
	time.sleep(2)

	#获取截屏adb
	Popen('./adb.exe pull /sdcard/tyt/screenshot.png c:/tyt/screenshot.png')
	
	time.sleep(2)

	#打开图片
	if os.path.exists('C:/tyt/screenshot.png'):
		print('file is true')
		im = Image.open('C:/tyt/screenshot.png')
		im.show()

	#获取鼠标按下位置
	#获取鼠标抬起位置
	#计算距离
	while True:
		key = input('please input any key to record the START POINT\n')
		if key == ';':
			break
		else:
			x,y = pyautogui.position()
			X_start = x
			Y_start = y
			positionStr = 'X:' + str(X_start).rjust(4) + '  Y:' + str(Y_start).rjust(4)
			print(positionStr)
		

	while True:
		key = input('please input any key to record the END POINT\n')
		if key == ';':
			break
		else:
			x,y = pyautogui.position()
			X_end = x
			Y_end = y
			positionStr = 'X:' + str(X_end).rjust(4) + '  Y:' + str(Y_end).rjust(4)
			print(positionStr)

	base = X_start - X_end
	height = Y_start - Y_end
	distance = math.sqrt(base*base + height*height)
	print('distance : ' + str(distance))

	#距离/单位 得到时间
	jumplen = int(distance * 3.49)
	
	#长按adb
	Popen('./adb.exe shell input swipe 100 100 100 100 %s'%jumplen)
	
	os.remove('C:/tyt/screenshot.png')

	time.sleep(3)
