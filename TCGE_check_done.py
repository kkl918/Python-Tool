import os, sys, zipfile, pathlib, ftplib
from ftplib import FTP

test = r'C:\Users\RSLAB\Desktop\dir'

ftp_155 = ['140.116.228.155','geodac_uav','geodac5;4cl4','/GEODAC_UAV/2018']
ftp_139 = ['140.116.228.155','geodac','rsej0 hk45j/ vup ','/TCGEO']


othro_dir = r'/1.測繪產品/1.1.Ortho_正射影像(包含附加檔)'
model_dir = r'/1.測繪產品/1.8.3DModel_3D模型'

def TCGE_dir(title):
    
    ds_dir = r"\\140.116.228.155\geodac_uav\TCGE"
    
    # 第一層資料夾
    pathlib.Path(ds_dir + '\\' + title).mkdir(parents=True, exist_ok=0)


    #第二層資料夾 - othro 
    pathlib.Path(ds_dir + '\\' + title + '\\' + 'othro').mkdir(parents=True, exist_ok=0)

    
    #第三層資料夾 - othro - 數字編號
    # for i in range(1,6):
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'othro' + '\\' + str(i)).mkdir(parents=True, exist_ok=0)

    #第二層資料夾 - cad
    pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad').mkdir(parents=True, exist_ok=0)
    pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad' + '\\' + 'origin').mkdir(parents=True, exist_ok=0)
    pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad' + '\\' + 'output').mkdir(parents=True, exist_ok=0)

    #第二層資料夾 - model
    pathlib.Path(ds_dir + '\\' + title + '\\' + 'model').mkdir(parents=True, exist_ok=0)

def uav_done(info):
    ftp = FTP(info[0])
    ftp.login(info[1], info[2])
    ftp.encoding='utf-8'
    ftp.cwd(info[3])
    ftp_155      = ftp.nlst(info[3])
    ftp_155_TCGE = ftp.nlst('/GEODAC_UAV/TCGE')
    
    uav_done = []
    tcge     = []
    
    for file in ftp_155:
        # 找出TCGE相關資料夾後新增到uav_done
        if file[26:29] == '臺北市':
            uav_done.append(file[17:])
            name = file[17:]
            othro = file + othro_dir
            if [f for f in ftp.nlst(othro) if not f.startswith('.')] == []:
                print(name,'有缺少檔案!')
            else:
                pass
            kk = [k for k in uav_done if file[26:29] == '臺北市'] 
            for k in kk:
                print(k)
    # for folder in ftp_155_TCGE:
        # if folder[26:29] == '臺北市':
            # tcge.append(folder[17:])
            # #print(folder[17:])
            
    # # 比較uav_done, tcge
    # for index, i in enumerate(uav_done):
        # if i in tcge:
            # pass
        # else:
            # TCGE_dir(i)
            # print('mkdir in TCGE')

        
        
uav_done(ftp_155)

