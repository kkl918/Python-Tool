###################################################
where_file_u_put = r"C:\Users\RSLAB\Desktop\dir\\"
file = '20190219.dat'                             
###################################################



desk = where_file_u_put + file[:-3]+ "txt"
path = where_file_u_put + file 


def dms2dd(line):
    comma = []
    for i in range(0,len(line)):
        if line[i] == ',':
            comma.append(i)
            
    
    p = line[:comma[0]]
    y = line[comma[0]+1:comma[1]]
    x = line[comma[1]+1:comma[2]]
    z = line[comma[2]:]
    
    x_degree = float(x[0:3])
    x_minute = float(x[4:6])
    x_second = float(x[6:8]+ '.'+ x[8:])

    y_degree = float(y[0:2])
    y_minute = float(y[3:5])
    y_second = float(y[5:7]+ '.'+ y[7:])

    x_decimal = x_degree + x_minute/60 + x_second/3600
    y_decimal = y_degree + y_minute/60 + y_second/3600

    # print(y_degree,y_minute,y_second)
    # print(x_degree,x_minute,x_second)
    out = p+',BLh,'+str(y_decimal)[:11]+','+str(x_decimal)[:12]+''+z+'\n'
    print(out)
    return(out)
with open(path) as dat:
    with open(desk,'w') as output: 
        for i in dat.readlines():
            output.write(dms2dd(i[:-2]))
        
    
    
