#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox

title_bar = 'template title'

window = Tk()
window.geometry("480x320")
window.title(title_bar)

fuc_title = { '1':'讀取',
              '2':'空',
              '3':'空',
              '4':'空',
              '5':'重新開機',
              '6':'關機',
              '7':'空',
              '8':'空',
              '9':'空',
              '10':'結束'}

def shutdown():
    sudoPassword = '123456'
    command = 'shutdown now'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
     
def reboot():
    sudoPassword = '123456'
    command = 'reboot now'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))

def helloCallBack(title,msg):
    msg = messagebox.showinfo( title, mas) 

def quit():
    window.destry()


line_1 = 0
line_2 = 160
length = 25
height = 10

fuc_1  = Button(window, width = length, height = height, text = fuc_title['1'], command = hello).place(x = 0,y = line_1)

fuc_2  = Button(window, width = length, height = height, text = fuc_title['2'], command = hello).place(x = 160,y = line_1)

fuc_3  = Button(window, width = length, height = height, text = fuc_title['3'], command = hello).place(x = 320,y = line_1)

fuc_4  = Button(window, width = length, height = height, text = fuc_title['4'], command = hello).place(x = 0,  y= line_2)

fuc_5  = Button(window, width = length, height = height, text = fuc_title['5'], command = hello).place(x = 160,y = line_2)

fuc_6  = Button(window, width = length, height = height, text = fuc_title['6'], command = hello).place(x = 320,y = line_2)
'''
fuc_7  = Button(window, width = length, height = height, text = fuc_title['7'], command = hello).place(x = 300,y = line_2)
fuc_8  = Button(window, width = length, height = height, text = fuc_title['8'], command = hello).place(x = 350,y = line_2)
fuc_9  = Button(window, width = length, height = height, text = fuc_title['9'], command = hello).place(x = 400,y = line_2)
fuc_10 = Button(window, width = length, height = height, text = fuc_title['10'], command = quit).place(x = 450,y = line_2)
'''

window.mainloop()