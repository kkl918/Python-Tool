import os, sys, zipfile, pathlib
title = input("資料夾名稱: ")

ds_dir = r"\\140.116.228.155\geodac_uav\TCGE\UAV圖資"
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