########################################
## Created on 2019/04/03              ##
## author: Chia-Ching Lin             ##
##                                    ##
## 專案CHUNK名字必須與155上資料夾一致 ##
########################################

import os, sys, zipfile, pathlib, shutil
import PhotoScan
from tkinter.filedialog import *
from bs4 import BeautifulSoup
import requests 
import xml.etree.ElementTree as ET
from xml.dom import minidom

url_front = 'https://geodac.ncku.edu.tw/TCGEO/2019/'

tw97   = PhotoScan.CoordinateSystem("EPSG::3826")
ws84   = PhotoScan.CoordinateSystem("EPSG::3857")
crs = PhotoScan.CoordinateSystem('LOCAL_CS["Local CS",LOCAL_DATUM["Local Datum",0],UNIT["metre",1]]')


path = r'\\140.116.228.155\geodac_uav\2019'
dir  = r'C:\Users\RSLAB\Desktop\dir\\'

dir_1   = '1.測繪產品'
dir_1_1 = '1.1.Ortho_正射影像(包含附加檔)'
dir_1_2 = '1.2.OrigPhoto_原始照片'
dir_1_3 ='1.3.PrecEval_精度評估報告'
dir_1_4 ='1.4.ContCoor_控制點座標)'
dir_1_5 ='1.5.ContPhoto_控制點照片'
dir_1_6 ='1.6.FlyRec_飛行記錄'
dir_1_7 ='1.7.DSM_數值地表模型'
dir_1_8 ='1.8.3DModel_3D模型'


print("\n- - - - - - - - Script started - - - - - - - - \n")

# init tree
root = ET.Element('tree',id="0")


def add_3D(name, date, wgs84, othro_location, cad_location, model_location, output):
    # check(dic['othro']+'index.html')
    # check(dic['cad'])
    # check(dic['model']+'tileset.json')
    one = ET.SubElement(root, "item", text = name, id = name, nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
    ET.SubElement(one , "item", text = '正射影像_' + date + '(雙擊定位)'       ,  id = wgs84 + ';;18@TileImage_ps@' + othro_location ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    ET.SubElement(one , "item", text = '工程圖說'                              ,  id = wgs84 + ';;18@kml@'          + cad_location   ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    ET.SubElement(one , "item", text = '3D_模型'                               ,  id = wgs84 + ';;18@3DModel@'      + model_location ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open(output, 'a',encoding = 'utf8') as myXML:
        myXML.write(xmlstr)

def add_2D(dic):
    one = ET.SubElement(root, "item", text=dic['text'], id=dic['text'], nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
    check(dic['othro']+'index.html')
    #check(dic['cad']) 
    ET.SubElement(one  , "item", text = '正射影像_' + dic['date'] + '(雙擊定位)',  id=dic['lt']+';;18@TileImage+ps@'+dic['othro'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    #ET.SubElement(one  , "item", text = '工程圖說'                              ,  id=dic['lt']+';;18@kml@'      +dic['cad']  ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    return 0

def pprint(x):
    xmlstr = minidom.parseString(x).toprettyxml(indent="   ")
    print(xmlstr)

def output_xml(x):
    xmlstr = minidom.parseString(x).toprettyxml(indent="   ")
    with open(path  + "output.xml", "w") as f:
        f.write(xmlstr)
    print('輸出完成!')
    
def get_wgs84(kml):
    with open(kml, 'r',encoding = 'utf8')as f:
        soup   = BeautifulSoup(f.read(), 'html.parser')
        lon    = soup.select('longitude')[0].text
        lat    = soup.select('latitude')[0].text
        wgs84  = lat+ ';' + lon 
        return wgs84


def create_upload(path, i):
    upload = os.path.join(path, i, '1.測繪產品', '1.8.3DModel_3D模型', 'upload'         )      
    othro  = os.path.join(path, i, '1.測繪產品', '1.8.3DModel_3D模型', 'upload', i, 'othro')
    cad    = os.path.join(path, i, '1.測繪產品', '1.8.3DModel_3D模型', 'upload', i, 'cad'  )
    model  = os.path.join(path, i, '1.測繪產品', '1.8.3DModel_3D模型', 'upload', i, 'model')
    
    # create folder in 155 for moving
    pathlib.Path(upload).mkdir(parents=True, exist_ok=1)
    pathlib.Path(othro).mkdir(parents=True, exist_ok=1)
    pathlib.Path(cad).mkdir(parents=True, exist_ok=1)
    pathlib.Path(model).mkdir(parents=True, exist_ok=1)
    
    
def create_xml(i, wgs84):
    # create each location in ftp
    othro_location = os.path.join(url_front, i, 'othro/').replace('\\', '/')
    cad_location   = os.path.join(url_front, i, 'cad/'  ).replace('\\', '/')
    model_location = os.path.join(url_front, i, 'model/').replace('\\', '/')
    
    # output file path
    output         = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\'  + r'upload\xml.txt'                           
    
    # chunkname date wgs84 othro_location cad_location model_location outputFile
    add_3D(i, i[0:8], wgs84, othro_location, cad_location, model_location, output)


def copytree_exist_folder(src,dst):
    if os.path.exists(src):
        
        # if dst folder is emty rm it
        if not os.listdir(dst):
            os.rmdir(dst)
            shutil.copytree(src, dst)
    
def export():
    
    for chunk in PhotoScan.app.document.chunks:
        # -> i = chunkname = folder name in 155 <- #
        for i in os.listdir(path):
            if i == chunk.label:
                    # 1.1.Ortho_正射影像
                    #------- 路徑 ---- 資料夾檔名 - 1.測繪產品 ------ 1.1 ----- 檔案名稱+副檔名 
                    othro  = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.tif'
                    tile   = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.zip'
                    report = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_3 + '\\' + i + '.pdf'
                    kmz    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.kmz'
                    
                    # 1.7.DSM_數值地表模型
                    dsm    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_7 + '\\' + i + '.tif'
                    
                    # 1.8.3DModel_3D模型
                    obj    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + 'model' + '.obj'
                    kmz_3d = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i + '.kmz'
                    

                    # 讀取中心座標    
                    kml = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i + '\\' + 'doc.kml'
                    with open(kml, 'r',encoding = 'utf8')as f:
                        soup   = BeautifulSoup(f.read(), 'html.parser')
                        lon    = soup.select('longitude')[0].text
                        lat    = soup.select('latitude')[0].text
                        wgs84  = lat+ ';' + lon                      

                        
                        # create folder in 155 for moving
                        pathlib.Path(os.path.join(path, i , '1.測繪產品', '1.8.3DModel_3D模型', 'upload'         )).mkdir(parents=True, exist_ok=0)
                        pathlib.Path(os.path.join(path, i , '1.測繪產品', '1.8.3DModel_3D模型', 'upload', 'othro')).mkdir(parents=True, exist_ok=0)
                        pathlib.Path(os.path.join(path, i , '1.測繪產品', '1.8.3DModel_3D模型', 'upload', 'cad'  )).mkdir(parents=True, exist_ok=0)
                        pathlib.Path(os.path.join(path, i , '1.測繪產品', '1.8.3DModel_3D模型', 'upload', 'model')).mkdir(parents=True, exist_ok=0)
                        
                        # create each location in xml
                        othro_location = os.path.join(url_front, i, 'othro/').replace('\\', '/')
                        cad_location   = os.path.join(url_front, i, 'cad/'  ).replace('\\', '/')
                        model_location = os.path.join(url_front, i, 'model/').replace('\\', '/')
                        
                        # output file path
                        output         = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\'  + r'upload\xml.txt'                           
                        
                        # chunkname date wgs84 othro_location cad_location model_location outputFile
                        add_3D(i, i[0:8], wgs84, othro_location, cad_location, model_location, output)
     
                    print('[OK] create myXML')

def find_folder():
    # i = chunkname = folder name in 155 
    for i in os.listdir(path)[7:-2]:
        # print(i)
        # where 3D model folder is
        model_folder  = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8
        upload_folder = os.path.join(model_folder,'upload')
        
        if len(os.listdir(os.path.join(upload_folder, i, 'othro'))) == 0:
            print(i)

        # # create upload folder
        create_upload(path, i)
        
        
        # check exist
        kml_folder = os.path.join(model_folder,i)
        if os.path.isdir(kml_folder):
            for kml in os.listdir(kml_folder):
                if kml.endswith('kml') and os.path.isfile(os.path.join(kml_folder,kml)):
                        kml = os.path.join(kml_folder,kml)
                        wgs84 = get_wgs84(kml)
                        create_xml(i, wgs84)
        
        print('[Start move tile.]')    
        # move tile data to dst
        tile_src = os.path.join(path, i, dir_1, dir_1_1, i)
        tile_dst = os.path.join(upload_folder, i, 'othro')
        copytree_exist_folder(tile_src, tile_dst)

        
def main():
    #export()
    find_folder()

main()

print("\n- - - - - - - - Script End - - - - - - - - \n")