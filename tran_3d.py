import sys, os, pathlib, shutil,subprocess, time
from subprocess import PIPE
from ftplib import FTP

def get_pos(line):
    comma = []
    for i in range(0,len(line)):
        if line[i] == ',':
            comma.append(i)


def move_155_to_174():
    path_155 = r'\\140.116.228.155\geodac_uav\2018'
    path_174 = r'\\140.116.228.174\geodac_data_test\RAW\RSImage\UAV\3DModel'
    
    comma = []
    mission_name      = []
    model_patn_in_155 = []
    cmd               = []


    with open(r'C:\Users\RSLAB\Desktop\2018_3D_Model.csv') as file:
        for line in file.readlines():  
            for i in range(0,len(line)):
                if line[i] == ',':
                    num+=1
                    

            #mission_name.append(line[i+1:-1])
                        #print(line[i+1:])
        #print(mission_name)

        

    # for i in os.listdir(path_155):
        #(i)
        # if i in mission_name:
            # print(i)
            # dir_174 = os.path.join(path_174,i)
            # print(dir_174)
            
            # pathlib.Path(dir_174).mkdir(parents=True, exist_ok=1)
            # m = os.path.join(path_155,i,'1.測繪產品','1.8.3DModel_3D模型')
            # for item in os.listdir(m):

                # if item[-3:] == 'txt':
                    # lat = item[0:13]
                    # lon = item[14:28]
                    # tran = "ssh user1@140.116.228.180 -p 2202 './trans3d "+i+' '+lon+' '+lat+"'\n"
                    # cmd.append(tran)
                
                ##shutil.copyfile(src, dst)  
                # elif item[-3:] == 'obj':
                    # shutil.copyfile(os.path.join(m,item),os.path.join(dir_174,item))

                # elif item[-3:] == 'mtl':
                    # shutil.copyfile(os.path.join(m,item),os.path.join(dir_174,item))
                # elif item[-3:] == 'jpg':
                    # shutil.copyfile(os.path.join(m,item),os.path.join(dir_174,item))
    # with open(r'C:\Users\RSLAB\Desktop\t.csv','a') as out:
        # for i in cmd:
            # out.write(i)


def call_cmd():
    with open(r'C:\Users\RSLAB\Desktop\t.csv') as text:
        num = 0
        for i in text:
            num+=1
            print(num , '\t', i)
            subprocess.Popen('powershell.exe ' + text.readline(), stdout=PIPE, stderr=PIPE, stdin=PIPE)
            time.sleep(30)

def ff():
    mp = input('Here:')
    subprocess.Popen('powershell.exe ' + mp)  
    print('powershell.exe ' + mp)  
    

move_155_to_174()
# call_cmd()
