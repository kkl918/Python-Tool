############################################################
## Created on 2018/07/01
## author: Chia-Ching Lin
## 
## 專案CHUNK名字必須與155上資料夾一致
############################################################
import os, sys, zipfile
import PhotoScan
from tkinter.filedialog import *

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

    
# 自動產生 TIFF、KMZ、TILE(含解壓縮)
def export():
    for chunk in PhotoScan.app.document.chunks:
        for i in os.listdir(path):
            if i not in os.listdir(path):
                print('請創建相對應資料夾')

            if i == chunk.label:
                    # 1.1.Ortho_正射影像
                    othro  = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.tif'
                    tile   = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.zip'
                    report = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_3 + '\\' + i + '.pdf'
                    kmz    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '.kmz'
                    
                    # 1.7.DSM_數值地表模型
                    dsm    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_7 + '\\' + i + '.tif'
                    
                    # 1.8.3DModel_3D模型
                    obj    = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + 'model' + '.obj'
                    kmz_3d = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8 + '\\' + i + '.kmz'

                    chunk.exportOrthomosaic(othro,image_format=PhotoScan.ImageFormatTIFF,projection=tw97,raster_transform=PhotoScan.RasterTransformNone,write_kml=True,write_world=True)
                    print('[OK] export othro.')

                    chunk.exportOrthomosaic(kmz  ,format=PhotoScan.RasterFormatKMZ,raster_transform=PhotoScan.RasterTransformNone,write_kml=True,write_world=True)
                    print('[OK] export kmz.')

                    chunk.exportReport(report, title = i, description = 'Made by GEODAC')
                    print('[OK] export report.')

                    chunk.exportOrthomosaic(tile,format=PhotoScan.RasterFormatXYZ,image_format=PhotoScan.ImageFormatPNG,raster_transform=PhotoScan.RasterTransformNone,projection=ws84,write_kml=True)
                    print('[OK] export tile.')
                    
                    chunk.exportModel(obj   , binary=False, precision=6, texture_format=PhotoScan.ImageFormatJPEG, texture=True, normals=False, colors=False, cameras=False, udim=False, strip_extensions=False, format=PhotoScan.ModelFormatOBJ, projection=crs)
                    print('[OK] export obj.')

                    chunk.exportModel(kmz_3d   , binary=False, precision=6, texture_format=PhotoScan.ImageFormatJPEG, texture=True, normals=False, colors=False, cameras=False, udim=False, strip_extensions=False, format=PhotoScan.ModelFormatKMZ, projection=crs)
                    print('[OK] export kmz_3d.')
                    
                    with zipfile.ZipFile(tile, 'r') as zf:
                        os.mkdir(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i)
                        zf.extractall(path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_1 + '\\' + i + '\\')
                        print('[OK] unzip tile')
                        
def main():
    export()

main()

print("\n- - - - - - - - Script End - - - - - - - - \n")