######### 编辑图形界面 ########
# import tkinter
# from tkinter import *
# top = tkinter.Tk()
# top.title("机器人控制界面")
# top.geometry('500x500+10+10')
# canvas = tkinter.Canvas(top,height=500,width=500)
# image = tkinter.PhotoImage(file="opi.gif")
# top.canvas.create_image(0,0, anchor='nw', image=image)#将图片置于画布上
# canvas.pack()
# top.update()
# lab1 = tkinter.Label(top,text="机器人控制显示",bg="green",fg="red",font=('黑体',20))
# lab1.pack(side=TOP)
# ###当前大机械臂位置，当前小机械臂位置，发送位置数据，
# ####需分成2个区域，左侧大机械臂控制显示界面，右侧小机械臂控制显示界面
# fm = tkinter.Frame(top)
# fmlab1 = tkinter.Label(fm,text="kuangjia",bg="red")
# fmlab1.pack()
# fm.pack(side=RIGHT)
# bt1 = tkinter.Button(top, text="发送")
# bt1.pack(side=LEFT)
# bt2 = tkinter.Button(top, text="停止")
# bt2.pack()
#
# # 进入消息循环
# top.mainloop()


#试验
import tkinter as tk
from tkinter import *
mainwin = tk.Tk()

frame1 = tk.Frame(mainwin)
fm1label = tk.Label(frame1,text="机械臂跟随系统控制界面",bg="red",font=('黑体',20))
fm1label.pack()
frame1.pack(side=TOP)

#FRAME2
frame2 = tk.Frame(mainwin)
fm2left = tk.Frame(frame2)
fm2right = tk.Frame(frame2)
fm2left_top = tk.Frame(fm2left)
fm2left_botton = tk.Frame(fm2left)
fm2right_top = tk.Frame(fm2right)
fm2right_botton = tk.Frame(fm2right)

fm2left_toplab = tk.Label(fm2left_top,text="Small Robot Control")
fm2left_toplab.pack(side=TOP)
fm2left_top.pack(side=TOP)
fm2left_bottonentry = tk.Entry(fm2left_botton)
fm2left_bottonentry.pack()
fm2left_botton.pack(side=BOTTOM)
fm2left.pack(side=LEFT)

fm2right_toplab = tk.Label(fm2right_top,text="Big Robot Control")
fm2right_toplab.pack()
fm2right_top.pack(side=TOP)
fm2right_bottonentry = tk.Entry(fm2right_botton)
fm2right_bottonentry.pack()
fm2right_botton.pack(side=BOTTOM)
fm2right.pack(side=RIGHT)

frame2.pack(side=BOTTOM)



mainwin.mainloop()







#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from tkinter import *
# import hashlib
# import time
#
# LOG_LINE_NUM = 0
#
# class MY_GUI():
#     def __init__(self,init_window_name):
#         self.init_window_name = init_window_name
#
#
#     #设置窗口
#     def set_init_window(self):
#         self.init_window_name.title("文本处理工具_v1.2")           #窗口名
#         #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
#         self.init_window_name.geometry('1068x681+10+10')
#         #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
#         #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
#         #标签
#         self.init_data_label = Label(self.init_window_name, text="待处理数据")
#         self.init_data_label.grid(row=0, column=0)
#         self.result_data_label = Label(self.init_window_name, text="输出结果")
#         self.result_data_label.grid(row=0, column=12)
#         self.log_label = Label(self.init_window_name, text="日志")
#         self.log_label.grid(row=12, column=0)
#         #文本框
#         self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
#         self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
#         self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
#         self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
#         self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
#         self.log_data_Text.grid(row=13, column=0, columnspan=10)
#         #按钮
#         self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
#         self.str_trans_to_md5_button.grid(row=1, column=11)
#
#
#     #功能函数
#     def str_trans_to_md5(self):
#         src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
#         #print("src =",src)
#         if src:
#             try:
#                 myMd5 = hashlib.md5()
#                 myMd5.update(src)
#                 myMd5_Digest = myMd5.hexdigest()
#                 #print(myMd5_Digest)
#                 #输出到界面
#                 self.result_data_Text.delete(1.0,END)
#                 self.result_data_Text.insert(1.0,myMd5_Digest)
#                 self.write_log_to_Text("INFO:str_trans_to_md5 success")
#             except:
#                 self.result_data_Text.delete(1.0,END)
#                 self.result_data_Text.insert(1.0,"字符串转MD5失败")
#         else:
#             self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
#
#
#     #获取当前时间
#     def get_current_time(self):
#         current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#         return current_time
#
#
#     #日志动态打印
#     def write_log_to_Text(self,logmsg):
#         global LOG_LINE_NUM
#         current_time = self.get_current_time()
#         logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
#         if LOG_LINE_NUM <= 7:
#             self.log_data_Text.insert(END, logmsg_in)
#             LOG_LINE_NUM = LOG_LINE_NUM + 1
#         else:
#             self.log_data_Text.delete(1.0,2.0)
#             self.log_data_Text.insert(END, logmsg_in)
#
#
# def gui_start():
#     init_window = Tk()              #实例化出一个父窗口
#     ZMJ_PORTAL = MY_GUI(init_window)
#     # 设置根窗口默认属性
#     ZMJ_PORTAL.set_init_window()
#
#     init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
#
#
# gui_start()