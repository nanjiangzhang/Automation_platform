# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
# 背景
canvas = tk.Canvas(root, width=1200, height=900, bd=0, highlightthickness=0)
imgpath = '1573363756345.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)

canvas.create_image(700, 500, image=photo)
canvas.grid()
# entry = tk.Entry(root, insertbackground='blue', highlightthickness=2)
# entry.pack()

# canvas.create_window(100, 50, width=100, height=20)

root.mainloop()