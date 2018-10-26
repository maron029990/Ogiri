# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:38:26 2018

@author: 010180079
"""

#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter

def DeleteEntryValue(event):
    #エントリーの中身を削除
    EditBox.delete(0, tkinter.END)


root = tkinter.Tk()
root.title(u"HitoshiMatsumoto")
root.geometry("1080x540")

#ラベル
Static1 = tkinter.Label(text=u'おだいをにゅうりょくしてね', foreground='#ff0000', background='#ffaacc')
Static1.pack()

Static2 = tkinter.Label(text=u'こんな', foreground='#ff0000', background='#ffaacc')
Static2.pack()
EditBox = tkinter.Entry()
EditBox.pack()
Static3 = tkinter.Label(text=u'はいやだ', foreground='#ff0000', background='#ffaacc')
Static3.pack()

value = EditBox.get()

Button = tkinter.Button(text=u'Go!!')
Button.bind("<Button-1>",DeleteEntryValue)
Button.pack()

root.mainloop()