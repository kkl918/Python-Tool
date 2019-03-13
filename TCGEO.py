import os, sys, zipfile, pathlib, pprint, time

def move_to_TCGE():
    sr_dir = r'\\140.116.228.155\geodac_uav\2018'
    sr_dir_chiled = r'1.測繪產品\1.1.Ortho_正射影像(包含附加檔)'
    
    ds_dir = r'\\140.116.228.155\geodac_uav\TCGE'
    ds_dir_child = 'othro'

    for title in os.listdir(sr_dir):
        taipei = [ "台北" , "臺北"]
        if title[9:11] in taipei:        
            print(title)
    
    
    
def create_dir():
    title = input("資料夾名稱: ")

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

def check_exist():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sr_dir = r"\\140.116.228.155\geodac_uav\2018"
    ds_dir = r"\\140.116.228.155\geodac_uav\TCGE"

        
    no_ori_cad = ['無原始工程圖說:']
    no_out_cad = ['無轉檔工程圖說:']
    no_othro   = ['無正射影像:']
    have_model = ['有三維模型:']
    
    for title in os.listdir(ds_dir):
        taipei  = [ "台北" , "臺北"]
        cad_ori = 'cad\origin'
        cad_out = 'cad\output'
        othro   = 'othro'
        model   = 'model'
        
        if title[9:11] in taipei:
            ori_check   = os.path.join(ds_dir,title,cad_ori) 
            out_check   = os.path.join(ds_dir,title,cad_out)
            othro_check = os.path.join(ds_dir,title,othro)
            model_check = os.path.join(ds_dir,title,model)
            # for cad
            if [f for f in os.listdir(ori_check) if not f.startswith('.')] == []:
                if not title.endswith(')'):
                    no_ori_cad.append(title)
            elif [f for f in os.listdir(out_check) if not f.startswith('.')] == []:
                no_out_cad.append(title)
            
            # for othro
            if [f for f in os.listdir(othro_check) if not f.startswith('.')] == []:
                no_othro.append(title)
            
            #for model
            if [f for f in os.listdir(model_check) if not f.startswith('.')] == []:
                pass
            else:
                have_model.append(title)

    check_list = os.path.join(ds_dir,'圖說確認清單.txt')
    with open (check_list, 'a', encoding = 'utf8') as cl:            
        cl.write('--------------------'+now+'--------------------\n')
        for i in no_ori_cad:
            cl.write(i+'\n')

        cl.write('-----------------------------------------------------------\n')
        for j in no_out_cad:
            cl.write(j+'\n')
            
        cl.write('-----------------------------------------------------------\n')
        for k in no_othro:
            cl.write(k+'\n')
        
        cl.write('-----------------------------------------------------------\n')
        for l in have_model:
            cl.write(l+'\n')            
        cl.write('--------------------------- ' + 'end' +' ---------------------------\n\n')
def main():
    check_exist()
        
main()    

## no use
# for title in os.listdir(sr_dir):
    # taipei = [ "台北" , "臺北"]
    # if title[9:11] in taipei:
        # # 第一層資料夾 |--- othro --- number_dir
        # #              |--- cad   ---| origin
        # #              |             | output
        # #              |--- model        
        
        # # 第一層資料夾
        # pathlib.Path(ds_dir + '\\' + title).mkdir(parents=True, exist_ok=0)
        
        # #第二層資料夾 - othro 
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'othro').mkdir(parents=True, exist_ok=0)
        
        # #第三層資料夾 - othro - 數字編號
        # for i in range(1,6):
            # pathlib.Path(ds_dir + '\\' + title + '\\' + 'othro' + '\\' + str(i)).mkdir(parents=True, exist_ok=0)
        
        # #第二層資料夾 - cad
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad').mkdir(parents=True, exist_ok=0)
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad' + '\\' + 'origin').mkdir(parents=True, exist_ok=0)
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'cad' + '\\' + 'output').mkdir(parents=True, exist_ok=0)
        
        # #第二層資料夾 - model
        # pathlib.Path(ds_dir + '\\' + title + '\\' + 'model').mkdir(parents=True, exist_ok=0)
        
