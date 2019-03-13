#!/usr/bin/python3
import shutil, pathlib, os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

title_bar = 'Observation Tools'

window = Tk()
window.geometry("600x25")
window.title(title_bar)
#window.withdraw()



fuc_title = { '1':'打開檔案',
              '2':'選取資料夾',
              '3':'標準化資料夾',
              '4':'dirs',
              '5':'空',
              '6':'結束',
              '7':'空',
              '8':'空',
              '9':'空',
              '10':'結束'}

def hello():
    msg = messagebox.showinfo( '訊息視窗' ,  '先空著') 

def helloCallBack(title,msg):
    msg = messagebox.showinfo( title, mas) 

def open_file():
    filename = askopenfilename()
    print(filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read())

def open_dir():
    dirname = askdirectory()
    print(dirname)
    return dirname
    
def std_folder():
    dir = open_dir()

    name = input('資料夾名稱:')
    #pathlib.Path(dir+ name).mkdir(parents=True, exist_ok=0
    pathlib.Path(dir+ '\\' +name + '/1.測繪產品').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/2.環景照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/3.一般產品').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/4.影片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/Photoscan').mkdir(parents=True, exist_ok=0)
    open(dir+ '\\' + name + '\\Photoscan' + '\\' + name + '.psx','w')
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.1.Ortho_正射影像(包含附加檔)').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.2.OrigPhoto_原始照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.3.PrecEval_精度評估報告').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.4.ContCoor_控制點座標)').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.5.ContPhoto_控制點照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.6.FlyRec_飛行記錄').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.7.DSM_數值地表模型').mkdir(parents=True, exist_ok=0)
    pathlib.Path(dir+ '\\' + name + '/1.測繪產品' + './1.8.3DModel_3D模型').mkdir(parents=True, exist_ok=0)

    
    return  messagebox.showinfo( '訊息視窗' ,  '完成標準化視窗')

def copy_file():
    src  = '.\e-GNSS三圍座標轉換預處理V3.exe'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    converter = dir_path + '\\' + src
    if os.path.isfile(converter):
        print(converter)
        copy = shutil.copyfile(converter,dst)
    else:
        print('找不到e-GNSS三圍座標轉換預處理V3.exe')
    
def dirs():
    print(os.system('dir'))
    print(os.path.realpath(__file__))
    
def quit():
    window.destroy()


line_1 = 0
line_2 = 100

length = 13
height = 1

fuc_1  = Button(window, width = length, height = height, text = fuc_title['1'], command = open_file).place(x = 0  ,y = line_1)

fuc_2  = Button(window, width = length, height = height, text = fuc_title['2'], command = open_dir ).place(x = 100,y = line_1)

fuc_3  = Button(window, width = length, height = height, text = fuc_title['3'], command = std_folder).place(x = 200,y = line_1)

fuc_4  = Button(window, width = length, height = height, text = fuc_title['4'], command = dirs).place(x = 300,y= line_1)

fuc_5  = Button(window, width = length, height = height, text = fuc_title['5'], command = copy_file).place(x = 400,y = line_1)

fuc_6  = Button(window, width = length, height = height, text = fuc_title['6'], command = quit ).place(x = 500,y = line_1)


window.mainloop()