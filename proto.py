# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:03:43 2018

@author: 010180079
"""

import tkinter as tk
import serial_test2
import threading


def pushed(self):
 print("clicked")
 self["text"] = "押されたよ"
 if self==button1:
     label = tk.Label(root, text="考え中1")
     label.grid()
     thread_1 = threading.Thread(target=serial_test2.func)
     thread_1.start()
 else:
     label = tk.Label(root, text="考え中2")
     label.grid()

root = tk.Tk()
#ウィンドウ表示
root.title("Hitoshi Matsumoto Ver.0")
root.geometry("1080x540")

label = tk.Label(root, text="お題をクリックしてください")
label.grid(row=0, column=40)

button1 = tk.Button(root, text="野球", command= lambda : pushed(button1))
button1.grid(row=10, column=40,padx=5, pady=5, sticky=tk.W+tk.E)
button2 = tk.Button(root, text="サッカー", command= lambda : pushed(button2))
button2.grid(row=20, column=20)
 



root.mainloop()