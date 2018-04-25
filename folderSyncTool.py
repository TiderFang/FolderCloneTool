# /usr/bin/env python
# -*- coding:utf-8 -*-

#1.get the target folder path and destination folder path
#2.check whether the destination foler exit 
#if the target folder not exit then
# 	exit or back to the first step
# end_if
#if the destination folder not exit then
# 	create the destination folder
# end_if
#get all files name into list in the target folder in the first level
#get all folder name into list in the target folder in the first level
# update files into destination folder 
# update folder into destination folder
# end

#code begin

#1.get the target folder path and destination folder path
import os
import tkinter.messagebox 
from tkinter import filedialog  
import shutil
def getdirname(targetdir):
	id = 0
	NotIN = 0
	while True:
		try:
			if targetdir.find('\\') != -1:
				id = targetdir.index('\\',id+1,len(targetdir))
			else:
				id = targetdir.index('/',id+1,len(targetdir))
		except:
			break
	name = targetdir[id+1:len(targetdir)]
	return name

def update(targetdirt,destindirt):
	targetdir = targetdirt
	destindir = destindirt
	print(destindir)
	targetfiles = os.listdir(targetdir)
	destinfiles = os.listdir(destindir)
	print(targetfiles)
#取出目标
	for prey in targetfiles:
#如果是文件类型：执行下列
		print(prey)
		os.chdir(targetdir)
		if os.path.isfile(prey):
			#检查目标文件是否存在于目标文件夹
			if prey in destinfiles:
				#检查更新日期
				src = targetdir+'/'+prey
				des = destindir+'/'+prey
				targettime = os.stat(src).st_mtime
				destintime = os.stat(des).st_mtime
				if targettime > destintime:
					shutil.copy(src,des)
				else:
					pass
			#如果文件不存在，直接拷贝
			else:
				src = targetdir+'/'+prey
				print(destindir)
				des = destindir+'/'+prey
				shutil.copy(src,des)
				pass
#如果是文件夹类型：执行下列
		os.chdir(targetdir)
		if os.path.isdir(prey):
			#如果文件夹存在：
			if prey in destinfiles :
					src = targetdir+'/'+prey
					des = destindir+'/'+prey
					update(src,des)
			else:
					src = targetdir+'/'+prey
					des = destindir+'/'+prey
					os.mkdir(des)
					update(src,des)
#递归循环


print("tell me where is the target folder?")
default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
tkinter.messagebox.showinfo('提示',"请选择要同步的文件夹")
targetdir = filedialog.askdirectory(title='选择要同步目标文件夹',initialdir=(os.path.expanduser(default_dir)))
tkinter.messagebox.showinfo("提示","请选择同步结果位置")
destindir = filedialog.askdirectory(title='选择要结果位置',initialdir=(os.path.expanduser(default_dir)))
#2.check whether the destination folder exit
## 获取目标文件夹的名称
## 检查目的地文件夹是否存在
targetdirname = getdirname(targetdir)
if targetdir not in destindir:
## 获取目的地文件夹中所有文件夹名字,检查是否包含目标文件夹名字
	destinfiles = os.listdir(destindir)

	if (targetdirname not in destinfiles) :
		os.mkdir(destindir+'/'+targetdirname)
		destindir = destindir+'/'+targetdirname
	else:
		destindir = destindir+'/'+targetdirname

	#3.获取所有目标文件及文件夹的名字
	#targetfiles = os.listdir(targetdir)
	#destinfiles = os.listdir(destindir)
	update(targetdir,destindir)
else:
	tkinter.messagebox.showwarning('错误',"不允许结果位置为目标文件夹的子文件夹,\n请选择其他同步位置")




