# -*- coding:utf8 -*-

import tkinter as tk
import time
from tkinter import *
from public import *
from threading import Thread
from PIL import Image, ImageTk
lable_msg_window = None


#  *------------------------------此处为功能函数------------------------------*  #
def close_button():

    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)


def ping():  # ping测试(免用户登录)

    lab_msg.set('正在连接站点....')

    if net_check('172.18.40.1') == 0:
        if net_check('39.107.236.6') == 0:

            lable_msg_window['bg'] = 'light green'
            lab_msg.set('Successful')
            close_button()
    else:

        lable_msg_window['bg'] = 'red'
        lab_msg.set('FAIL')


def login_usr():  # 用户名和密码的校验

    global check_point
    lab_msg.set('正在登录.....')
    if str(en_user.get()) == '1380':
        if str(en_pasw.get()) == '1380':
            check_point = 0
        else:
            lable_msg_window['bg'] = 'red'
            lab_msg.set('FAIL')
    else:
        lable_msg_window['bg'] = 'red'
        lab_msg.set('FAIL')
    if check_point == 0:
        if net_check('39.107.236.6') == 0:
            lable_msg_window['bg'] = 'light green'
            lab_msg.set('Login Successful')
            close_button()
        else:
            lable_msg_window['bg'] = 'red'
            lab_msg.set('FAIL')


def thread_ping(func, *args):  # 免密码登录时加入线程
    t = Thread(target=func, args=args, daemon=True)
    t.start()


def thread_login(func, *args):  # 输入用户名和密码后的校验
    t1 = Thread(target=func, args=args, daemon=True)
    t1.start()


#  *------------------------------此处为功能函数------------------------------*  #


root = tk.Tk()
root.geometry('1200x900')  # 窗体大小
root.iconbitmap('log.ico')  # 图标
root.title('XXXXXXXXXXXXXXXXX')  # title
root['background'] = 'white'  # 主窗体背景
root.resizable(0, 0)  # 窗口不可操作，限制拖动

#  message框
lab_msg = StringVar()  # 账户输入框

lf_lable = tk.LabelFrame(root, width=400, height=150, text='Consequence')  # 外框线
lf_lable.grid(row=1, column=0, sticky='w', padx=10, pady=10)  # 外框线位置

lable_msg_window = tk.Label(lf_lable, textvariable=lab_msg, bg='white', font=('Arial', 21), width=20, height=2, relief='ridge',
                            padx=20, pady=20, borderwidth=10)  # 判断当前网络是正确
lab_msg.set('NA')
lable_msg_window.place(x=6, y=1)  # 内置窗口位置
#  message框
#  登录框
lf_lable_Settings = tk.LabelFrame(root, width=400, height=300, text='Login User')  # 外框线
lf_lable_Settings.grid(row=2, column=0, sticky='w', padx=10, pady=10)  # 外框线位置
#  登录功能框
#  用户名密码输入框
lab_user = Label(root, text="账户:")
en_user = StringVar()  # 账户输入框
ent_user = Entry(root, width=30, text=en_user)
lab_passw = Label(root, text="密码:")
en_pasw = StringVar()  # 密码输入框
ent_passw = Entry(root, width=30, text=en_pasw, show = "*")
lab_user.place(x=50, y=250)
ent_user.place(x=100, y=250)
lab_passw.place(x=50, y=300)
ent_passw.place(x=100, y=300)
#   #############
#  #登录以及测试按钮
button1 = tk.Button(root,  # 连接（不需要输入用户名密码）
                    text='连接',
                    width=10,
                    height=4,
                    command=lambda: thread_ping(ping)  # ping按钮（测试按钮）
                    )
button1.place(x=40, y=360)
button2 = tk.Button(root,  # 连接（不需要输入用户名密码）
                    text='登录',
                    width=10,
                    height=4,
                    command=lambda: thread_login(login_usr)  # ping按钮（测试按钮）
                    )
button2.place(x=280, y=360)
#  #读取远端的服务器中内容，并分为两个不同标签+
lf_lable_value = tk.LabelFrame(root, width=400, height=390, text='Content')  # 外框线
lf_lable_value.grid(row=3, column=0, sticky='w', padx=10, pady=10)  # 外框线位置

#  ##############
root.mainloop()

if __name__ == '__main__':
    pass
