########################################
## Created on 2019/02/26              ##
## author: Chia-Ching Lin             ##
## Arrange log from pixhawk           ##
## change output with accZ+9.8        ##
########################################
import os
from math import tan, sin, cos, radians

# where .py is
py_path = os.path.dirname(os.path.realpath(__file__))

# output file path
output = os.path.join(py_path,"log_tw97.txt")

# init some emty value 
tt = ''
compare = 0 
GPS_xyz = ', 0, 0, 0, 0'
GPS_time = 0
ATT_time = 0

class LatLonToTWD97(object): # class for convert

# This object provide method for converting lat/lon coordinate to TWD97
# coordinate
# The reference to:
# http://blog.ez2learn.com/2009/08/15/lat-lon-to-twd97/
# http://www.uwgb.edu/dutchs/UsefulData/UTMFormulas.htm


    def convert(self, lat, lon): # convert function
        """Convert lat lon to twd97
        """
        a = 6378137.0 # WGS84 Semi-major axis a(m)
        b = 6356752.314245 # WGS84 Semi-minor axis b(m)
        long0 = radians(121) # central meridian of zone
        k0 = 0.9999 # scale along central meridian of zone
        dx = 250000 # x offset(m)
        e = (1-b**2/(a**2))**0.5
        e2 = e**2/(1-e**2)
        n = (a-b)/(a+b)
        nu = a/(1-(e**2)*(sin(lat)**2))**0.5
        p = lon-long0
        A = a*(1 - n + (5/4.0)*(n**2 - n**3) + (81/64.0)*(n**4 - n**5))
        B = (3*a*n/2.0)*(1 - n + (7/8.0)*(n**2 - n**3) + (55/64.0)*(n**4 - n**5))
        C = (15*a*(n**2)/16.0)*(1 - n + (3/4.0)*(n**2 - n**3))
        D = (35*a*(n**3)/48.0)*(1 - n + (11/16.0)*(n**2 - n**3))
        E = (315*a*(n**4)/51.0)*(1 - n)
        S = A*lat - B*sin(2*lat) + C*sin(4*lat) - D*sin(6*lat) + E*sin(8*lat)
        K1 = S*k0
        K2 = k0*nu*sin(2*lat)/4.0
        K3 = (k0*nu*sin(lat)*(cos(lat)**3)/24.0) * (5 - tan(lat)**2 + 9*e2*(cos(lat)**2) + 4*(e2**2)*(cos(lat)**4))
        y = K1 + K2*(p**2) + K3*(p**4)
        K4 = k0*nu*cos(lat)
        K5 = (k0*nu*(cos(lat)**3)/6.0) * (1 - tan(lat)**2 + e2*(cos(lat)**2))
        x = K4*p + K5*(p**3) + dx

        return(x, y)


## 1136904794, 1.33, -1.11, 186.3, -0.06866664, 0.065655789.791234779, 22.9955167, 120.2227508, 23.35, 0.75, 1.33, -1.11, 186.29, -0.1546949, 0.09852124, -0.02695742, 2.264192, -4.878877, 1.831122


# open file
for item in os.listdir(py_path):
    if item.endswith('log'):
        file = os.path.join(py_path,item)
        print('OPEN: '+ file)

        ## start to process .log
        with open(file,'r') as log:
            with open(output,'a') as out:
                
                ## init a format header msg in txt 
                out.write('TimeUS, ATT_Roll(deg), ATT_Pitch(deg), ATT_Yaw(deg), AHRS_AcX(m/s/s), AHRS_AcY(m/s/s), AHRS_AcZ(m/s/s), Lat, Lon, GPS_Alt, HDOP(0~100, >3 bad), EKF_roll(deg), EKF_pitch(deg), EKF_yaw(deg), EKF_velN(m/s), EKF_velE(m/s), EKF_velD(m/s), EKF_posN(metres North), EKF_posE(metres East), EKF_posD(metres Down)\n')
                #out.write(roll(deg), pitch(deg), yaw(deg), velN(m/s), velE(m/s), velD(m/s),posD_dot(first derivative of down position), posN(metres North), posE(metres East), posD(metres Down), gyrX(cd/sec), gyrY(cd/sec), gyrZ(cd/sec), originHgt(WGS-84 altitude of EKF origin in cm))
                ## i means a single line in log, consider i as line
                for i in log.readlines():
                    if i[0:3] =='FMT':
                        if i[14:18] == 'GPS,':
                            pass
                        elif i[14:18] == 'ATT,':
                            pass
                        elif i[14:18] == 'IMU,':
                            pass
                    ## ATT FORMAT
                    ##       time     ro    pi    yaw       AcX        AcY        AcZ
                    ##     1         2    3     4      5           6          7          8
                    ## ATT, 77352318, 4.3, 5.12, 88.28, -0.0505647, -0.103724, -9.802816, 0, 0
                    
                    
                    elif i[0:3] == 'ATT':
                        count = 0
                        # j means comma position in line
                        for j in range(0,len(i)):
                            if i[j] == ',':
                                count+=1
                                if count   == 1:
                                    col_1 = j
                                elif count == 2:
                                    col_2 = j
                                    ATT_time = i[col_1+2:col_2]
                                    #print('ATT:'+ATT_time)
                                    ## 1-2 time
                                elif count == 7:
                                    col_7 = j
                                elif count == 8:
                                    col_8 = j
                                    ## midify accZ value with +9.8 and covert to string
                                    ATT_msg = i[5:col_7] + ', '+str(float(i[col_7+2:col_8])+9.8)
                                    if int(ATT_time) > int(GPS_time):
                                        #print(ATT_msg+GPS_xyz)
                                        #out.write(ATT_msg+GPS_xyz+'\n')
                                        tt = ATT_msg+GPS_xyz
                    
                    ## not use #############             
                    elif i[0:4] == 'IMU,':##
                        pass              ##
                        #print(i[:14])    ## 
                        #out.write(i)     ## 
                    elif i[0:4] == 'IMU2':##
                        pass              ## 
                        #print(i[:15])    ##
                        #out.write(i)     ##
                    ## until here ##########

                    # meet gps msg    
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
                                elif count == 8:
                                    col_8 = j
                                elif count == 9:
                                    col_9 = j
                                elif count == 10:
                                    col_10 = j
                                    # filter bad gps
                                    if float(GPS_dop[2:]) != 99.99 :
                                        
                                        # WGS 84
                                        #GPS_wgs84 = i[col_7:col_10]
                                        
                                        GPS_tw97 = LatLonToTWD97().convert(radians(float(i[col_7+1:col_8])), radians(float(i[col_8+1:col_9])))
                                        
                                        # tw97 neh
                                        GPS_xyz = str(GPS_tw97)[1:-1] + i[col_9:col_10]
                                        
                                        # tw97 neh + RGB
                                        GPS_xyzrgb = str(GPS_tw97)[1:-1] + ', ' +str(float(i[col_9+2:col_10])+20) + ', 255, 0, 0'
                                        #print(GPS_xyzrgb)
                                        
                                        # tw97 neh + hdop
                                        GPS_XYZ = GPS_xyz + GPS_dop
                                        #print(GPS_xyz)
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
                                elif count == 9:
                                    col_9 = j                                      
                                elif count == 12:
                                    col_12 = j
                                    EKF_msg = i[col_2:col_8]+i[col_9:col_12]
                                    #print(tt + EKF_msg)
                                    if GPS_xyz != ', 0, 0, 0, 0':
                                        # only write gps xyz
                                        out.write(GPS_xyzrgb+'\n')
                                        
                                        # write all msg
                                        # out.write(tt + EKF_msg+'\n')
                                        
                                  