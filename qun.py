# -*- coding: UTF-8 -*-
from PIL import Image
import random
import time
import os
import sys
import shutil
from zipfile import ZipFile
from os import listdir
from os.path import isfile, isdir, join

def addFileIntoZipfile(srcDir, fp):
    for subpath in listdir(srcDir):
        subpath = join(srcDir, subpath)
        if isfile(subpath):
            fp.write(subpath)
        elif isdir(subpath):
            fp.write(subpath)
            addFileIntoZipfile(subpath, fp)

def zipCompress(srcDir, desZipfile):
    fp = ZipFile(desZipfile, mode='a')
    addFileIntoZipfile(srcDir, fp)
    fp.close()

path = "E:/Py_Image/" +u"/群聊/微信图片" + str(int(time.time()))
dirpath = "E:\\Py_Image\\" + u"群聊".encode("gb2312")
if os.path.exists(dirpath):
	shutil.rmtree(dirpath)
	os.mkdir(dirpath)
else:
	os.mkdir(dirpath)
material = Image.open("E:/Py_Image/material/qun.jpg")
qun_box = (0,71,1080,214)
ex_box = (0,214,1080,1180)
qun_max = []
ex_max = []
for x in xrange(1,15):
    qun_max.append(str(x))
    pass
for x in xrange(1,20):
    ex_max.append(str(x))
    pass
a = {
	"1" : 147,
	"2" : 133,
	"3" : 87,
	"4" : 39,
	"5" : 56,
	"6" : 85,
	"7" : 44,
	"8" : 159,
	"9" : 271,
	"10" : 99,
	"11" : 111,
	"12" : 68,
	"13" : 79,
	"14" : 116,
	"15" : 85,
}
quns = random.sample(qun_max,8)
exquns = random.sample(ex_max,8)
sums = 0
s = 0
for qun in quns:
    sums = sums + a[qun]
    qun_im = Image.open("E:/Py_Image/quns/" + qun + ".jpg")
    qun_ex = Image.open("E:/Py_Image/quns/eximage/" + exquns[s] + ".jpg")
    m = qun_im.crop(qun_box)
    ex = qun_ex.crop(ex_box)
    material.paste(m,qun_box)
    material.paste(ex,ex_box)
    material.save(path + qun + ".jpg","JPEG")
    s = s + 1
    pass
paths = [ u"群聊".encode("gb2312"), u"朋友圈".encode("gb2312")]
t = time.strftime("%Y%m%d",time.localtime(time.time()))
zip_name = t + u"桐庐公司8群8圈".encode("gb2312") + str(sums) + u"人.zip".encode("gb2312")
for path in paths:
    zipCompress(path, zip_name)