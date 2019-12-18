import os, shutil

# src
F_path = r"F:\WorkFolder\2019_TCGE_UAV"
P_list = [p for p in os.listdir(F_path)]
P_path = [os.path.join(F_path, p, ('1.測繪產品'), ('1.1.Ortho_正射影像(包含附加檔)'), p + '.kmz') for p in P_list]

# dst
KmzFolder = r'C:\Users\RSLAB\Desktop\2019_TCGE_成果KMZ'
Kmz_path  = [os.path.join(KmzFolder, p + '.kmz') for p in P_list]

Src2Dst   = {}
num = 0
for i in P_path:
    for j in Kmz_path:
        if os.path.isfile(i) and i.split('\\')[-1] == j.split('\\')[-1]:
            print("[{}]\n{}\n{}\n".format(num, i ,j))
            shutil.copy(i, j)
            num = num +1

print(len(P_path))
# F:\WorkFolder\2019_TCGE_UAV\20190312_臺北市內湖區碧山段三小段\1.測繪產品\1.1.Ortho_正射影像(包含附加檔)