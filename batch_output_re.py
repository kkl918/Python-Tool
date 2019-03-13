########################################
## Created on 2018/07/01              ##
## author: Chia-Ching Lin             ##
##                                    ##
## 專案CHUNK名字必須與155上資料夾一致 ##
########################################
import os, sys, zipfile, pathlib
import PhotoScan
from tkinter.filedialog import *
from bs4 import BeautifulSoup

tw97   = PhotoScan.CoordinateSystem("EPSG::3826")
ws84   = PhotoScan.CoordinateSystem("EPSG::3857")
crs = PhotoScan.CoordinateSystem('LOCAL_CS["Local CS",LOCAL_DATUM["Local Datum",0],UNIT["metre",1]]')


path = r'\\140.116.228.155\geodac_uav\2018'
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

def workflow():
    pass

def create_dir(name):
    #pathlib.Path(path+ name).mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/2.環景照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/3.一般產品').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/4.影片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/Photoscan').mkdir(parents=True, exist_ok=0)
    #open('.\\'+ name + '\\Photoscan' + '\\' + name + '.psx','w')
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.1.Ortho_正射影像(包含附加檔)').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.2.OrigPhoto_原始照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.3.PrecEval_精度評估報告').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.4.ContCoor_控制點座標)').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.5.ContPhoto_控制點照片').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.6.FlyRec_飛行記錄').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.7.DSM_數值地表模型').mkdir(parents=True, exist_ok=0)
    pathlib.Path(path+'\\'+ name + '/1.測繪產品' + './1.8.3DModel_3D模型').mkdir(parents=True, exist_ok=0)

# 自動產生 TIFF、KMZ、TILE、MODEL(含解壓縮及中心座標檔案)
def export():
    for chunk in PhotoScan.app.document.chunks:
        for i in os.listdir(path):
            if i == chunk.label:
                    #create_dir(i)
                    
                    
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
                    
                    # 正射影像 TIFF
                    chunk.exportOrthomosaic(othro,image_format=PhotoScan.ImageFormatTIFF,projection=tw97,raster_transform=PhotoScan.RasterTransformNone,write_kml=True,write_world=True,white_background=False)
                    print('[OK] export othro.')
                    
                    # 正射影像 KMZ
                    chunk.exportOrthomosaic(kmz  ,format=PhotoScan.RasterFormatKMZ,raster_transform=PhotoScan.RasterTransformNone,write_kml=True,write_world=True)
                    print('[OK] export kmz.')

                    # 報告
                    chunk.exportReport(report, title = i, description = 'Made by GEODAC')
                    print('[OK] export report.')

                    # 圖專
                    chunk.exportOrthomosaic(tile,format=PhotoScan.RasterFormatXYZ,image_format=PhotoScan.ImageFormatPNG,raster_transform=PhotoScan.RasterTransformNone,projection=ws84,write_kml=True)
                    print('[OK] export tile.')
                    
                    # DSM
                    chunk.exportDem(path=dsm,format=PhotoScan.RasterFormatTiles,image_format=PhotoScan.ImageFormatTIFF,projection= tw97,nodata=-32767)
                    print('[OK] export dsm.')            
                    
                    #三維模型 OBJ
                    chunk.exportModel(obj   , binary=False, precision=6, texture_format=PhotoScan.ImageFormatJPEG, texture=True, normals=False, colors=False, cameras=False, udim=False, strip_extensions=False, format=PhotoScan.ModelFormatOBJ, projection=crs)
                    print('[OK] export obj.')

                    #三維模型 KMZ
                    chunk.exportModel(kmz_3d   , binary=False, precision=6, texture_format=PhotoScan.ImageFormatJPEG, texture=True, normals=False, colors=False, cameras=False, udim=False, strip_extensions=False, format=PhotoScan.ModelFormatKMZ, projection=crs)
                    print('[OK] export kmz_3d.')

                    # 解壓縮KMZ_3D
                    with zipfile.ZipFile(kmz_3d, 'r') as kmz:
                        pathlib.Path(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i).mkdir(parents=True, exist_ok=1)
                        #os.mkdir(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i)
                        kmz.extractall(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i + '\\')
                        print('[OK] unzip kmz_3d')
                                        

                    # 讀取中心座標    
                    kml = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i + '\\' + 'doc.kml'
                    with open(kml, 'r',encoding = 'utf8')as f:
                        #print(f.read())
                        soup = BeautifulSoup(f.read(), 'html.parser')
                        lon = soup.select('longitude')[0].text
                        lat = soup.select('latitude')[0].text
                        center = lat+ ',' + lon                      
                        output = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + center + '.txt'
                        open(output, 'a',encoding = 'utf8')
                        print('[OK] create center file')
                            
                        with open(r'\\140.116.228.155\geodac_uav\uav.txt', 'a', encoding = 'utf8') as txt:
                            txt.write(i + ',' + center+'\n')
                            print('[OK] add to uav.txt')

                    # 解壓縮圖專
                    print('Start unzip tile')
                    with zipfile.ZipFile(tile, 'r') as zf:
                        pathlib.Path(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i).mkdir(parents=True, exist_ok=1)
                        #os.mkdir(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i)
                        zf.extractall(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '\\')
                        print('[OK] unzip tile')
    
def main():
    export()

main()

print("\n- - - - - - - - Script End - - - - - - - - \n")