import os, sys
from ftplib import FTP

path_155 = r'\\140.116.228.155\geodac_uav\2019'
path_174_model = r'\\140.116.228.174\geodac_data_test\RAW\RSImage\UAV\3DModel'

info  = ['140.116.249.139','geodac','rsej0hk45j/vup','/TCGEO/2019']
ftp   = FTP(info[0])
ftp.login(info[1], info[2])
ftp.cwd(info[3])
ftp_list = ftp.nlst(info[3])

dir_1   = '1.測繪產品'
dir_1_1 = '1.1.Ortho_正射影像(包含附加檔)'
dir_1_2 = '1.2.OrigPhoto_原始照片'
dir_1_3 ='1.3.PrecEval_精度評估報告'
dir_1_4 ='1.4.ContCoor_控制點座標)'
dir_1_5 ='1.5.ContPhoto_控制點照片'
dir_1_6 ='1.6.FlyRec_飛行記錄'
dir_1_7 ='1.7.DSM_數值地表模型'
dir_1_8 ='1.8.3DModel_3D模型'

def uploadThis(path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        if os.path.isfile(path + r'\{}'.format(f)):
            fh = open(f, 'rb')
            ftp.storbinary('STOR %s' % f, fh)
            fh.close()
        elif os.path.isdir(path + r'\{}'.format(f)):
            ftp.mkd(f)
            ftp.cwd(f)
            uploadThis(path + r'\{}'.format(f))
    ftp.cwd('..')
    os.chdir('..')


for dir in os.listdir(path_174_model):
    src = os.path.join(path_174_model, dir)
    dst = r'/TCGEO/2019' + '/' + dir + '/model'
    if dir in ftp_list: 
        ftp.cwd(dst)
        if len(os.listdir(src)) > 0:
            print(os.listdir(src),dst)
            uploadThis(src)

# error      = []
# ready2send = []
# print('[num]\t [name]')
# for i in os.listdir(path)[4:-2]:
    # model_folder  = path + '\\' + i + '\\' + dir_1 + '\\'+ dir_1_8
    # target = os.path.join(model_folder,'upload',i)
    # if os.listdir(target) and os.listdir(os.path.join(target,'othro')):
        # print(len(os.listdir(os.path.join(target,'othro'))), '\t', i[:40])
        # ready2send.append(os.path.join(path,i))
    # elif not os.listdir(os.path.join(target,'othro')):
        # error.append(i)


# check error
# if len(error) != 0:
    # print('\n[Error]')
    # for i in error:
        # print(i[:40])
# print('\n\n[Excute]')
# for i in ready2send:
    # if os.path.isdir(i):
        # print(i)
        # uploadThis(i)
    # else:
        # print('[Error]:',i)
