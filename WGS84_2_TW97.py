TWD97轉Lat/Lon(Python):
# 98257023
# Feng-Yu Yang
# 2012-04-08
# Edit Victor's file
# Convert Lat/Lon to TWD97
from math import tan, sin, cos, radians # Using math.tan, math.sin, math.cos, math.radians
kkk = open('nccu_UTF8.txt') # Open input file > kkk. The data format must be "name lat lon"
fout = open('NCCU-TWD97.txt','w') # Create a new file for converted coordinates(TWD97)

for line in kkk:
t = line.split() # separate each column, using "space"
class LatLonToTWD97(object): # class for convert
"""
This object provide method for converting lat/lon coordinate to TWD97
coordinate
The reference to:
http://blog.ez2learn.com/2009/08/15/lat-lon-to-twd97/
http://www.uwgb.edu/dutchs/UsefulData/UTMFormulas.htm
"""

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

return x, y

if __name__ == '__main__':
c = LatLonToTWD97()
lat = radians(float(t[1]))
lon = radians(float(t[2]))
x, y = c.convert(lat, lon)
print t[0],'Input(lat/lon):', t[1], t[2], ' Output(TWD97):', x, y

f = '''%s Input(lat/lon): %s %s Output(TWD97): %s %s \n''' % (t[0], t[1], t[2], x, y)

fout.write(str(f))
kkk.close()
fout.close()