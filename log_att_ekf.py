import os

# where .py is
py_path = os.path.dirname(os.path.realpath(__file__))

# output file path
output = os.path.join(py_path,"log.txt")

# pos = location_xyz(GPS) + AHRS(ATT) 
tt = ''
compare = 0 
GPS_xyz = ', x, x, x, x'
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
                out.write('TimeUS, ATT_Roll(deg), ATT_Pitch(deg), ATT_Yaw(deg), AHRS_AcX(m/s/s), AHRS_AcY(m/s/s), AHRS_AcZ(m/s/s), Lat, Lon, GPS_Alt, HDOP(0~100, >3 bad), EKF_roll(deg), EKF_pitch(deg), EKF_yaw(deg), EKF_velN(m/s), EKF_velE(m/s), EKF_velD(m/s), EKF_posN(metres North), EKF_posE(metres East), EKF_posD(metres Down)\n')
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
                                        #out.write(ATT_msg+GPS_xyz+'\n')
                                        tt = ATT_msg+GPS_xyz
                                        
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
                                elif count == 6:
                                    col_6 = j
                                elif count == 7:
                                    col_7 = j
                                    GPS_dop = i[col_6:col_7]
                                elif count == 10:
                                    col_10 = j
                                    #if float(GPS_dop) < 6 :
                                    GPS_xyz = i[col_7:col_10]
                                    GPS_xyz = GPS_xyz + GPS_dop
                    elif i[0:3] == 'NKF':
                        count = 0
                        for j in range(0,len(i)):
                            if i[j] == ',':
                                count+=1
                                if count   == 1:
                                    col_1 = j

                                elif count == 2:
                                    col_2 = j
                                elif count == 7:
                                    col_7 = j
                                elif count == 8:
                                    col_8 = j                                    
                                elif count == 11:
                                    col_11 = j
                                    EKF_msg = i[col_2:col_8]+i[col_8:col_11]
                                    #print(tt + EKF_msg)
                                    out.write(tt + EKF_msg+'\n')
                                  