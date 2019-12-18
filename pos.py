
raw_file = r'C:\Users\RSLAB\Desktop\photo_20190522_162335_remove.txt'
out_file = r'C:\Users\RSLAB\Desktop\pos_remove.txt'

# DSC01172.JPG
with open(raw_file, 'r') as f:
    with open(out_file, 'w') as w:
        num = 1172
        for line in f.readlines():
            
            for item in line.split('\t')[:11]:
                w.write(item + '\t')
            w.write('DSC0'+ str(num) +'.jpg')
            num = num + 1
            w.write('\n')    
            # print(f.readline().split('\t')[10])
    