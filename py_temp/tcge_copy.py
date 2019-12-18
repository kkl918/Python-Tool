import os, shutil, pathlib, subprocess, zipfile
from osgeo import gdal
from osgeo import gdal,ogr,osr
import numpy as np

# 資料夾規則: 日期 經度 緯度 層數 版本 資料夾資訊
# 20170418_121066563_022894010_14_000_RSImage_UAV_Ortho

# 通用
desktop    = r'C:\Users\RSLAB\Desktop'
tile_csv   = r'C:\Users\RSLAB\Desktop\TCGE_batch_upload\tif.csv'


# 2018
src_2018    = r'\\140.116.228.155\geodac_uav\2018'
dst_2018    = r'C:\Users\RSLAB\Desktop\TCGE_2018_UAV'
ls_155_2018      = os.listdir(src_2018)
tile_dst_2018 = r'H:\TCGE\TCGE_2018_UAV\tile'
tif_dst_2018  = r'H:\TCGE\TCGE_2018_UAV\tif'
target_path_2018 = [r"{}\{}".format(src_2018, single_dir) for single_dir in ls_155_2018 if os.path.isdir(r"{}\{}".format(src_2018, single_dir))]
target_name_2018 = [single_dir for single_dir in ls_155_2018 if os.path.isdir(r"{}\{}".format(src_2018, single_dir))]



# 2019
src = r'\\140.116.228.155\geodac_uav\2019'
dst  = r'C:\Users\RSLAB\Desktop\TCGE_batch_upload'

src_img = r'1.測繪產品\1.1.Ortho_正射影像(包含附加檔)'
src_mdl = r'\1.測繪產品\1.8.3DModel_3D模型'
ls_155 = os.listdir(src)
target_path = [r"{}\{}".format(src, single_dir) for single_dir in ls_155 if os.path.isdir(r"{}\{}".format(src, single_dir))]
target_name = [single_dir for single_dir in ls_155 if os.path.isdir(r"{}\{}".format(src, single_dir))]


# pathlib.Path(tile_dst).mkdir(parents=True, exist_ok=1)
# pathlib.Path(tif_dst).mkdir(parents=True, exist_ok=1)

# name2index   = {}
# name2newname = {}

# with open("{}\{}".format(desktop, "\\tcge_ua.csv"), "r") as index:
        # for i in index :
            # # 中文檔名對應:[(1)編號 (2)政規化檔名]
            # name2index[i.split(',')[1][:-1]] = [i.split(',')[0]]

# with open("{}\{}".format(desktop, "\\檔名.csv"), "r") as index:
        # for i in index :
            # # 中文檔名對應:[(1)編號 (2)政規化檔名]
            # # name2newname[i.split(',')[1][:-4]] = [i.split(',')[3]]
            # # print(i.split(',')[1][:-4] , i.split(',')[3])
            # cn_dir_name     = i.split(',')[1][:-4].encode('utf-8')
            # create_dir_name = i.split(',')[3][:-1].encode('utf-8')
            # # print(type(create_dir_name))
            # # print(tile_dst+'\\'+create_dir_name)
            # # pathlib.Path(tile_dst+'\\'+create_dir_name).mkdir(parents=True, exist_ok=1)
            # for item in target_path:
                # # print(item.split('\\')[-1].encode('utf-8'))
                # if cn_dir_name == item.split('\\')[-1].encode('utf-8'):
                    # # print("{}\{}\{}.zip".format(item, src_img,item.split('\\')[-1]))
                    # zip = "{}\{}\{}.zip".format(item, src_img,item.split('\\')[-1])
                    # if os.path.isfile(zip):
                        # # 建立資料夾
                        # dst = tile_dst+'\\'+create_dir_name.decode('utf-8')
                        # pathlib.Path(dst).mkdir(parents=True, exist_ok=1)
                        
                        # # print(dst,'\n',zip)
                        # print(dst)
                        # with zipfile.ZipFile(zip, 'r') as zf:
                            # zf.extractall(dst)
                            # print('[OK] unzip tile')
                            
            
# print(name2newname)            



# yi_file = r'C:\Users\RSLAB\Desktop\易辛\RSImage_UAV_Ortho.csv'
# with open(yi_file, 'r') as yi:
    # for i in yi:
        # # print(i.split(',')[0].split('\\')[-1]+'.tif')
        # tif = i.split(',')[0].split('\\')[-1]+'.tif'
        # if tif in name2newname.keys():
            # print(name2newname.keys())
        
      


def GetExtent(gt,cols,rows):
    ''' Return list of corner coordinates from a geotransform

        @type gt:   C{tuple/list}
        @param gt: geotransform
        @type cols:   C{int}
        @param cols: number of columns in the dataset
        @type rows:   C{int}
        @param rows: number of rows in the dataset
        @rtype:    C{[float,...,float]}
        @return:   coordinates of each corner
    '''
    ext=[]
    xarr=[0,cols]
    yarr=[0,rows]

    for px in xarr:
        for py in yarr:
            x=gt[0]+(px*gt[1])+(py*gt[2])
            y=gt[3]+(px*gt[4])+(py*gt[5])
            ext.append([x,y])
            # print(x,y)
        yarr.reverse()
    return ext

def ReprojectCoords(coords,src_srs,tgt_srs):
    ''' Reproject a list of x,y coordinates.

        @type geom:     C{tuple/list}
        @param geom:    List of [[x,y],...[x,y]] coordinates
        @type src_srs:  C{osr.SpatialReference}
        @param src_srs: OSR SpatialReference object
        @type tgt_srs:  C{osr.SpatialReference}
        @param tgt_srs: OSR SpatialReference object
        @rtype:         C{tuple/list}
        @return:        List of transformed [[x,y],...[x,y]] coordinates
    '''
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    for x,y in coords:
        x,y,z = transform.TransformPoint(x,y)
        trans_coords.append([x,y])
    return trans_coords

# raster=r'C:\Users\RSLAB\Desktop\TCGE_batch_upload\Raw\RSImage\UAV\Ortho\20190107_河川局.tif'
def get_meta(raster):    
    ds=gdal.Open(raster)

    gt=ds.GetGeoTransform()

    cols = ds.RasterXSize
    rows = ds.RasterYSize
    ext=GetExtent(gt,cols,rows)

    src_srs=osr.SpatialReference()
    src_srs.ImportFromWkt(ds.GetProjection())
    #tgt_srs=osr.SpatialReference()
    #tgt_srs.ImportFromEPSG(4326)
    tgt_srs = src_srs.CloneGeogCS()

    geo_ext=ReprojectCoords(ext,src_srs,tgt_srs)
    meta = [geo_ext[0], geo_ext[2], [(geo_ext[0][0]+geo_ext[2][0])/2, (geo_ext[0][1]+geo_ext[2][1])/2]]
    # print(meta[0], meta[1], meta[2])
    return meta

def main():
    num = 0
    with open(tile_csv, 'w') as tile_csv: 
        for i in target_name:
            file_location = i[9:12]
            # print(file_location)
            if file_location == "臺北市" or file_location == "國立政":
            
                file_date  = i[:8]
                file_year  = i[:4]
                file_month = i[4:6]
                file_day   = i[6:8]
                


                
                # print(file_date, file_year, file_month, file_day)
                
                src_tif  = "{}\{}\{}\{}.{}".format(src, i, src_img, i, "tif")
                src_tile = "{}\{}\{}\{}.{}".format(src, i, src_img, i, "zip")
                
                dst_tif  = "{}\{}.{}".format(tif_dst, i, "tif")
                dst_tile = "{}\{}.{}".format(tile_dst, i, "zip")

                print(i)
                LeftGeo    = "N/A"
                RightGeo   = "N/A"
                TopGeo     = "N/A"
                BottomGeo  = "N/A"
                CenterGeoX = "N/A"
                CenterGeoY = "N/A"
                sol        = "N/A"
                
                if os.path.isfile(src_tif) and os.path.isfile(src_tile):
                    # print(num , "|", src_tif.split("\\",-1)[-1], src_tile.split("\\",-1)[-1], '\n')
                    # print(num , "|", dst_tif.split("\\",-1)[-1], src_tile.split("\\",-1)[-1], '\n')
                    # print(num , "|", dst_tif, dst_tile)
                    # 原檔案位置,新檔案位置,圖磚位置,LeftGeo,RightGeo,TopGeo,BottomGeo,CenterGeoX,CenterGeoY,解析度,年,月,日,地名,COUNTY, TOWN, VILLAGE, 分局名稱, Subbasinna, 
                    write2csv_1 = "{},{},{},".format(dst_tif, "N/A", dst_tile)
                    write2csv_2 = "{},{},{},{},{},{},{},".format(LeftGeo, RightGeo, TopGeo, BottomGeo, CenterGeoX, CenterGeoY, sol)
                    write2csv_3 = "{},{},{},{}\n".format(file_year, file_month, file_day, i)
                    write2csv   = write2csv_1 + write2csv_2 + write2csv_3
                    # print(write2csv)
                    # tile_csv.write(write2csv)
                    # if not os.path.isfile(dst_tif):
                    shutil.copyfile(src_tif,dst_tif)
                    # elif not os.path.isfile(dst_tile):    
                    # shutil.copyfile(src_tile,dst_tile)
                num = num + 1

def main_2018():

    name2id = {}
    with open("{}\{}".format(desktop, "\\tcge_ua.csv"), "r") as index:
            for i in index :
                # 中文檔名對應:(1)編號
                name2id[i.split(',')[1][:-1]] = i.split(',')[0]


    for i in target_path_2018:
            file_location = i.split('\\')[-1][9:12]
            file_name     = i.split('\\')[-1]
            # print(file_location)
            
            # if file_location == "臺北市":
                # if file_name[-1] == ')':
                    # tif     = "{}\{}\{}.tif".format(i, src_img, file_name)
                    # tile    = "{}\{}\{}.zip".format(i, src_img, file_name) 
                    # if os.path.isfile("{}\{}\{}.tif".format(i, src_img, file_name)):
                        # file_name = file_name[:-3]
                        # dst_tif  = "{}\{}.tif".format(tif_dst_2018,  file_name)
                        # dst_tile = "{}\{}.zip".format(tile_dst_2018, file_name)
                        # print(i)
                # else:
            tif     = "{}\{}\{}.tif".format(i, src_img, file_name)
            tile    = "{}\{}\{}.zip".format(i, src_img, file_name) 
            if os.path.isfile("{}\{}\{}.tif".format(i, src_img, file_name)):
                
                dst_tif  = "{}\{}.tif".format(tif_dst_2018,  file_name)
                dst_tile = "{}\{}.zip".format(tile_dst_2018, file_name)
                # pathlib.Path().mkdir(parents=True, exist_ok=1)
                # print(i)
                if not os.path.isfile(dst_tif):
                    print(tif, '\n',dst_tif,'\n\n')
                    shutil.copyfile(tif, dst_tif)
                    print(tif, '\n',dst_tif,'\n\n')
                    shutil.copyfile(tile,dst_tile)
 
                        # # print(file_name)
                        # if file_name[9:] in name2id.keys():
                            # tcge = r'C:\Users\RSLAB\Desktop\TCGE'
                            # new  = "{}\{}".format(tcge, id)
                            # print(file_name[9:],name2id[file_name[9:]])
                        # pathlib.Path().mkdir(parents=True, exist_ok=1)
                        # print(tile)

def std_dir():
    name2id = {}
    with open("{}\{}".format(desktop, "\\tcge_ua.csv"), "r") as index:
            for i in index :
                # 中文檔名對應:(1)編號
                name2id[i.split(',')[1][:-1]] = i.split(',')[0]
                
    for i in name2id.keys():
        
        id_name = "{}_{}".format(name2id[i],i).replace(":", "").replace("\"", "")
        tcge = r'C:\Users\RSLAB\Desktop\TCGE'
        new  = "{}\{}".format(tcge, id_name)
        pathlib.Path(new).mkdir(parents=True, exist_ok=1)
        print(new)
        
        
        
        
main_2018() 
# std_dir()   