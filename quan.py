'''微信朋友圈图片批量生成'''
# -*- coding: UTF-8 -*-
from PIL import Image
import random
import time
import os
import sys
import shutil
# 转发内容1坐标
an_box = (170,1250,1070,1500)
# 转发内容2坐标
an_box2 = (170,1650,1070,1900)
# 任务栏坐标
ex_box = (0,0,1080,71)

# 生成文件的名称和路径
path = "E:/Py_Image/" +u"/朋友圈/微信图片" + str(int(time.time()))
# 读取已有图像的路径
dirpath = "E:\\Py_Image\\" + u"朋友圈".encode("gb2312")
'''对保存文件目录进行检测'''
if os.path.exists(dirpath):
	shutil.rmtree(dirpath)
	os.mkdir(dirpath)
else:
	os.mkdir(dirpath)
'''读取转发素材并复制'''
material = Image.open("E:/Py_Image/material/friend.jpg")
m = material.crop(an_box)

andorid = ["1","2","3","4","5","6","7","8",]
# 其他内容文件名称（1-15）
exans = []
for x in xrange(1,15):
	exans.append(str(x))
	pass
'''随机从中读取8个图像素材'''
an = random.sample(andorid,8)
exan = random.sample(exans,8)

s = 0
# 批量替换和生成新的图像
for a in an:
	an_im = Image.open("E:/Py_Image/friends/Android/"+a+".jpg")
	an_ex = Image.open("E:/Py_Image/friends/Android/eximage/" + exan[s] + ".jpg")
	ex = an_ex.crop(ex_box)
	an_im.paste(m,an_box)
	an_im.paste(m,an_box2)
	an_im.paste(ex,ex_box)
	an_im.save(path + a + ".jpg","JPEG")
	s = s + 1
	pass

#ios_box = (122,820,726,920)
#IOS = ["1","2","3","4","5","6",]
#ios = random.sample(IOS,4)
#n = material.crop(an_box2)
# for i in ios:
# 	ios_im = Image.open("E:/Py_Image/friends/IOS/"+i+".jpg")
# 	ios_im.paste(n,ios_box)
# 	ios_im.save(path + "0" + i + ".jpg","JPEG")
# 	pass