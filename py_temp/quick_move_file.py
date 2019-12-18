import os, zipfile

index  = r'\\Pc-tcgeo\tcge\TCGE\TCGE_2018_UAV_正規化\108檔名.csv'

src    = r'\\Pc-tcgeo\TCGE\TCGE\TCGE_2018_UAV\tile'
dst    = r'\\Pc-tcgeo\TCGE\TCGE\TCGE_2018_UAV\done'

target_tile = os.listdir(r'\\Pc-tcgeo\tcge\TCGE\TCGE_2018_UAV\tile')

with open(index, 'r') as f:
    for line in f:
        num  = line.split(',')[0]
        ori  = line.split(',')[1][:-4]
        aft  = line.split(',')[2]
        tile = line.split(',')[3]
        dst_path = '{}\{}'.format(dst, tile)
        
        # print(num, ori, tile_path)
        
        for i in target_tile:
            src_path = "{}\{}".format(src, i)
            if i[:-4] == ori and  os.path.isfile(src_path):
                    print("{}/{}".format(num,len(target_tile)))
                    print(src_path)
                    print(dst_path)
                    # with zipfile.ZipFile(src_path, 'r') as zf:
                        # zf.extractall(dst_path[:-2])
                        # print('[OK] unzip tile\n\n')
                    

       
