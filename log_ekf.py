import os

# where .py is
py_path = os.path.dirname(os.path.realpath(__file__))

# output file path
output = os.path.join(py_path,"log_ekf.txt")

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
                #out.write('FORMAT:TimeUS,Roll(deg),Pitch(deg),Yaw(deg),AcX(m/s/s),AcY(m/s/s),AcZ(m/s/s),Lat,Lon,Alt\n')
                out.write(roll(deg), pitch(deg), yaw(deg), velN(m/s), velE(m/s), velD(m/s),posD_dot(first derivative of down position), posN(metres North), posE(metres East), posD(metres Down), gyrX(cd/sec), gyrY(cd/sec), gyrZ(cd/sec), originHgt(WGS-84 altitude of EKF origin in cm))
                ## i = a single line in log 
                for i in log.readlines():
                    if i[0:3] =='FMT':
                        if i[14:18] == 'GPS,':
                            pass
                        elif i[14:18] == 'ATT,':
                            pass
                        elif i[14:18] == 'IMU,':
                            pass
                    ## meet EKF1
                    elif i[0:3] == 'EKF1':
                        #out.write(i[4:]+'\n')
                        print(i[4:]+'\n')
