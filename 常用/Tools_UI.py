#!/usr/bin/python3
import shutil, pathlib, os, webbrowser, glob, subprocess, datetime
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import pandas as pd

import osr, os, affine, time
import numpy as np
from matplotlib import pyplot as plt
from gdalconst import *
from osgeo import gdal

from subprocess import PIPE

title_bar = 'ob tools'

window = Tk()
window.geometry("600x25")
window.title(title_bar)
#window.withdraw()



fuc_title = { '1':'選擇資料夾',
              '2':'執行轉換',
              '3':'橢球高',
              '4':'正高',
              '5':'KML_Add',
              '6':'Tran3D',
              '7':'index',
              '8':'空',
              '9':'空',
              '10':'結束'}

src_dst = []

src_name = ''

def src():
    src_name = askopenfilename()
    print(src_name)

def dst():
    dst_name = askdirectory()
    src_dst.append(dst_name)
    print(src_dst[1]) 
    
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
    
def egnss_7():
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
                df.to_csv(r'C:\Users\RSLAB\Desktop\used_橢球高.csv', sep=',',header=None, index=None, encoding='utf-8')
                
def egnss_8():
    desktop = r'C:\Users\RSLAB\Desktop'
    os.chdir(desktop)
    for file in glob.glob("*.csv"):
            if file[0:4] == '三維坐標':
                #print(file)
                os.rename(file, 'origin.csv')
                df = pd.read_csv(r'C:\Users\RSLAB\Desktop\origin.csv',encoding = 'big5')
                print(df,'\n')
                col = [0,2,3,4,8] # 8->正高 7->橢球高
                df = df.drop(df.columns[col], axis = 1)
                print(df,'\n')
                df.to_csv(r'C:\Users\RSLAB\Desktop\used_正高.csv', sep=',',header=None, index=None, encoding='utf-8')

                print(df,'\n')
                col = [0,2,3,4,7] # 8->正高 7->橢球高
                df = df.drop(df.columns[col], axis = 1)
                print(df,'\n')
                df.to_csv(r'C:\Users\RSLAB\Desktop\used_橢球高.csv', sep=',',header=None, index=None, encoding='utf-8')
    
def quit():
    window.destroy()

def open_url():
    url = r'https://egnss.nlsc.gov.tw/trans/threeD.aspx'
    webbrowser.open_new_tab(url)

def dms2dd(line):
    comma = []
    for i in range(0,len(line)):
        if line[i] == ',':
            comma.append(i)
            
    
    p = line[:comma[0]]
    y = line[comma[0]+1:comma[1]]
    x = line[comma[1]+1:comma[2]]
    z = line[comma[2]:]
    
    x_degree = float(x[0:3])
    x_minute = float(x[4:6])
    x_second = float(x[6:8]+ '.'+ x[8:])

    y_degree = float(y[0:2])
    y_minute = float(y[3:5])
    y_second = float(y[5:7]+ '.'+ y[7:])

    x_decimal = x_degree + x_minute/60 + x_second/3600
    y_decimal = y_degree + y_minute/60 + y_second/3600

    # print(y_degree,y_minute,y_second)
    # print(x_degree,x_minute,x_second)
    out = p+',BLh,'+str(y_decimal)[:11]+','+str(x_decimal)[:12]+''+z+'\n'
    print(out)
    return(out)
    
def do_dms2dd():
    path = askopenfilename()
    new_name = path[:-4]+'_conv.txt'
    with open(path) as dat:
        with open(new_name,'w') as output: 
            for i in dat.readlines():
                output.write(dms2dd(i[:-2]))    
    output.close()
    open_url()


def get_lon_lat(file_in, file_out, data): 
    with open(file_in, 'r', encoding='utf8') as origin:
        with open(file_out, 'w', encoding='utf8') as out:
            num = 0
            for line in origin.readlines():  
                if num == 1 :
                    out.write('\t\t\t\t\t\t\t')
                    for j in line.split():
                            if j != '</LineString>' and j != '</coordinates>':
                                xlon = float(j.split(',')[0])
                                xlat = float(j.split(',')[1])
                                print(xlon, xlat)
                                
                                h    = str(retrieve_pixel_value((xlon, xlat), data)+0.7)        
                                out.write(j.split(',')[0] + ',' + j.split(',')[1] + ',' + h + ' ')  
                    # out.write('</coordinates>')
                    num = 0
                else:                   
                    if line.find('<outline>0</outline>') > 0:
                        pass
                    else:
                        out.write(line) 
                
                if line.find('<coordinates>') > 0:
                    num = 1
    print('[OK] write kml.\n')

def retrieve_pixel_value(geo_coord, data_source):
    """Return floating-point value that corresponds to given point."""
    x, y = geo_coord[0], geo_coord[1]
    forward_transform =  affine.Affine.from_gdal(*data_source.GetGeoTransform())
    reverse_transform =  ~forward_transform
    px, py = reverse_transform * (x, y)
    px, py = int(px + 0.5), int(py + 0.5)
    pixel_coord = px, py
    data_array = np.array(data_source.GetRasterBand(1).ReadAsArray())
    # i = data_array[0]
    # j = data_array[1]
    return(data_array[pixel_coord[1]][pixel_coord[0]])

def funtion_kml_add_height():    
      
    kml_file   = askopenfilename()
    kml_out    = kml_file[:-4] + '_addHeight' + kml_file[-4:]
    dem_file   = askopenfilename()
    start_time = time.time() 
    data  = gdal.Open(dem_file, GA_ReadOnly)
    array = get_lon_lat(kml_file, kml_out, data)
   
    print("--- %s seconds ---" % (time.time() - start_time))

def funtion_kml_index():    
    lon = input('Lon:')  
    lat = input('Lat:')
    wgs = [float(lon),float(lat)]
    dem_file   = askopenfilename() 
    data  = gdal.Open(dem_file, GA_ReadOnly)
    print(retrieve_pixel_value(wgs , data))

def tran_3d():
    path_174 = r'\\140.116.228.174\geodac_data_test\RAW\RSImage\UAV\3DModel'
    folder = askdirectory()
    nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    tran = ''
    # print(folder, '\n\n', nowtime)
    for item in os.listdir(folder):
        dir_174 = os.path.join(path_174, nowtime)
        pathlib.Path(dir_174).mkdir(parents=True, exist_ok=1)
        if item[-3:] == 'txt':
            lat = item[0:13]
            lon = item[14:28]
            tran = "ssh user1@140.116.228.180 -p 2202 './trans3d "+ nowtime +' '+lon+' '+lat+ "'"


        if item[-3:] == 'obj':
            shutil.copyfile(os.path.join(folder,item),os.path.join(dir_174,item))
        elif item[-3:] == 'mtl':
            shutil.copyfile(os.path.join(folder, item),os.path.join(dir_174,item))
        elif item[-3:] == 'jpg':
            shutil.copyfile(os.path.join(folder, item),os.path.join(dir_174,item))
        
    print(tran)
    # process  = subprocess.Popen('powershell.exe ' + tran, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    # out, err = process.communicate()
    # print('[stdout]: ', out)
    # print('[stderr]: ', err)
    # print('\n')

# init condition    
line_1 = 0
line_2 = 100

length = 13
height = 1

fuc_1  = Button(window, width = length, height = height, text = fuc_title['2'], command = do_dms2dd ).place(x = 0  ,y = line_1)

fuc_2  = Button(window, width = length, height = height, text = fuc_title['3'], command = egnss_7 ).place(x = 100,y = line_1)

fuc_3  = Button(window, width = length, height = height, text = fuc_title['4'], command = egnss_8).place(x = 200,y = line_1)

fuc_4  = Button(window, width = length, height = height, text = fuc_title['5'], command = funtion_kml_add_height).place(x = 300,y = line_1)

fuc_5  = Button(window, width = length, height = height, text = fuc_title['6'], command = tran_3d).place(x = 400,y = line_1)

fuc_6  = Button(window, width = length, height = height, text = fuc_title['7'], command = funtion_kml_index).place(x = 500,y = line_1)

window.mainloop()