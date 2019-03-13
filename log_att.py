import os

# where .py is
py_path = os.path.dirname(os.path.realpath(__file__))

# output file path
output = os.path.join(py_path,"log.txt")

# pos = location_xyz(GPS) + AHRS(ATT) 

compare = 0 
GPS_xyz = ', 0, 0, 0'
GPS_time = 0
ATT_time = 0
for item in os.listdir(py_path):
    if item.endswith('log'):
        file = os.path.join(py_path,item)
        print('OPEN: '+ file)

        ## start to process .log
        with open(file,'r') as log:
            with open(output,'a') as out:
                
                ## init a format msg in txt 
                out.write('TimeUS,Roll(deg),Pitch(deg),Yaw(deg),AcX(m/s/s),AcY(m/s/s),AcZ(m/s/s),Lat,Lon,Alt\n')
                #out.write(roll(deg), pitch(deg), yaw(deg), velN(m/s), velE(m/s), velD(m/s),posD_dot(first derivative of down position), posN(metres North), posE(metres East), posD(metres Down), gyrX(cd/sec), gyrY(cd/sec), gyrZ(cd/sec), originHgt(WGS-84 altitude of EKF origin in cm))
                ## i = a single line in log 
                for i in log.readlines():
                    if i[0:3] =='FMT':
                        if i[14:18] == 'GPS,':
                            pass
                        elif i[14:18] == 'ATT,':
                            pass
                        elif i[14:18] == 'IMU,':
                            pass
                    ## meet ATT
                    elif i[0:3] == 'ATT':
                        count = 0
                        for j in range(0,len(i)):
                            if i[j] == ',':
                                count+=1
                                if count   == 1:
                                    col_1 = j
                                elif count == 2:
                                    col_2 = j
                                    ATT_time = i[col_1+2:col_2]
                                    #print('ATT:'+ATT_time)
                                elif count == 8:
                                    col_8 = j
                                    ATT_msg = i[5:col_8]
                                    if int(ATT_time) > int(GPS_time):
                                        #print(ATT_msg+GPS_xyz)
                                        out.write(ATT_msg+GPS_xyz+'\n')
                                    
                                        
                    elif i[0:4] == 'IMU,':
                        pass
                        #print(i[:14])
                        #out.write(i)
                    elif i[0:4] == 'IMU2':
                        pass
                        #print(i[:15])
                        #out.write(i)
                    elif i[0:3] == 'GPS':
                        #print(i[:16]+i[46:77])
                        count = 0
                        for j in range(0,len(i)):
                            if i[j] == ',':
                                count+=1
                                if count   == 1:
                                    col_1 = j
                                    #print(i[:col_1])
                                elif count == 2:
                                    col_2 = j
                                    GPS_time = i[col_1+2:col_2]
                                    #print('GPS:'+GPS_time)
                                elif count == 7:
                                    col_7 = j
                                elif count == 9:
                                    col_9 = j
                                    GPS_xyz = i[col_7:col_10]
                    elif i[0:3] == 'NKF':
                        count = 0
                        for j in range(0,len(i)):
                            if i[j] == ',':
                                count+=1
                                if count   == 1:
                                    col_1 = j
                                    #print(i[:col_1])
                                elif count == 2:
                                    col_2 = j
                                    GPS_time = i[col_1+2:col_2]
                                    #print('GPS:'+GPS_time)
                                elif count == 7:
                                    col_7 = j
                                elif count == 8:
                                    col_8 = j                                    
                                elif count == 10:
                                    col_10 = j
                                    EKF_msg = i[col_1:col_7]+i[col_8:col_10-1]
                                    print(EKF_msg)
                                  