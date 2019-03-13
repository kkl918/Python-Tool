#!/usr/bin/python3
import shutil, pathlib, os, webbrowser, glob
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from dirsync import sync
import pandas as pd

title_bar = 'ob tools'

window = Tk()
window.geometry("600x25")
window.title(title_bar)
#window.withdraw()



fuc_title = { '1':'來源資料夾',
              '2':'目的資料夾',
              '3':'EGNSS',
              '4':'EGNSS(1)',
              '5':'EGNSS(2)',
              '6':'結束',
              '7':'空',
              '8':'空',
              '9':'空',
              '10':'結束'}

src_dst = []

def src():
    src_name = askdirectory()
    src_dst.append(src_name) 
    print(src_dst[0])


def dst():
    dst_name = askdirectory()
    src_dst.append(dst_name)
    print(src_dst[1])
    

def sync_dir():
    sync(src_dst[0], src_dst[1], 'sync')
    print('sync done.')
    os.system('exit')

# def sync_dir():
    # sync(askdirectory(), askdirectory(), 'sync')
    # print('sync done.')
    
def egnss_1():
    #dir = r'C:\Users\RSLAB\Desktop\新增資料夾'
    dir = askdirectory()
    shutil.copy('D:\EGNSS\e-GNSS三圍座標轉換預處理V3.exe', dir)
    os.chdir(dir)
    #----------
    for file in glob.glob("*.dat"):
        dat  = dir + '/' + file
        print(dat)
        df = pd.read_csv(dat, header=None, sep=",",encoding = 'big5')
        df.columns = ["a", "b", "c", "d", "e"]
        #print(df,'\n')
        
        list = []
        for i in df[df.columns[0]]:
            if i[0:4] == 'Base':
                pass
                #print(i)
            else:
                list.append(i)

        for i in list:
         print(i)
        df = df[df.a.isin(list)]
        print(df,'\n')
        df.to_csv(dir + '\\' + file, sep=',',header=None, index=None, encoding='utf-8')
    #----------
    os.system('start ' + dir + '\\'+ 'e-GNSS三圍座標轉換預處理V3.exe')
    url = r'https://egnss.nlsc.gov.tw/trans/threeD.aspx'
    webbrowser.open_new_tab(url)
    
def egnss_2():
    desktop = r'C:\Users\RSLAB\Desktop'
    os.chdir(desktop)
    for file in glob.glob("*.csv"):
            if file[0:4] == '三維坐標':
                #print(file)
                os.rename(file, 'origin.csv')
                df = pd.read_csv(r'C:\Users\RSLAB\Desktop\origin.csv',encoding = 'big5')
                print(df,'\n')
                col = [0,2,3,4,7] # 8->正高 7->橢球高
                df = df.drop(df.columns[col], axis = 1)
                print(df,'\n')
                df.to_csv(r'C:\Users\RSLAB\Desktop\used.csv', sep=',',header=None, index=None, encoding='utf-8')
    
def quit():
    window.destroy()

def open_url():
    url = r'https://egnss.nlsc.gov.tw/trans/threeD.aspx'
    webbrowser.open_new_tab(url)
    
    
line_1 = 0
line_2 = 100

length = 13
height = 1

fuc_1  = Button(window, width = length, height = height, text = fuc_title['1'], command = src ).place(x = 0  ,y = line_1)

fuc_2  = Button(window, width = length, height = height, text = fuc_title['2'], command = dst ).place(x = 100,y = line_1)

fuc_3  = Button(window, width = length, height = height, text = fuc_title['3'], command = open_url).place(x = 200,y = line_1)

fuc_4  = Button(window, width = length, height = height, text = fuc_title['4'], command = egnss_1).place(x = 300,y = line_1)

fuc_5  = Button(window, width = length, height = height, text = fuc_title['5'], command = egnss_2).place(x = 400,y = line_1)

fuc_6  = Button(window, width = length, height = height, text = fuc_title['6'], command = quit).place(x = 500,y = line_1)


window.mainloop()