# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt#使用系统自带的matplotlib.pyplot进行画图，这句相当于导入一个库
import numpy as np #导入numpy,并简称为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #设x范围为（0，3pi），样本数为100
y = np.sin(x)#y=sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#生成1行2列的2个子图，定位第1个图来进行操作
plt.title(r'$f(x)=sin(x)$') #显示图表的标题
plt.plot(x, y)#画出y相对于x的图像
#plt.show()

x1 = [t*0.375*np.pi for t in x]#设x1=0.375*pi*t,t=x,即,x1=0.375*pi*x
y1 = np.sin(x1)#y1=sin(x1)
plt.subplot(1,2,2)#生成1行2列的2个子图，定位第2个图来进行操作
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #显示图表的标题为f(x)=sin(ωx),ω=3/8pi
plt.plot(x, y1)#画出y1相对于x1的图像
plt.show()#显示生成的图像图片（不显示格式）