from osgeo import gdal
import osr
import numpy as np
from matplotlib import pyplot as plt
from gdalconst import *

filename = r'C:\Users\RSLAB\Desktop\WGS84.tif'
data = gdal.Open(filename, GA_ReadOnly)

raster  = data.GetRasterBand(1)
width   = data.RasterXSize
height  = data.RasterYSize
gt      = data.GetGeoTransform()
minX = gt[0]
minY = gt[3] + width*gt[4] + height*gt[5] 
maxX = gt[0] + width*gt[1] + height*gt[2]
maxY = gt[3] 

# print ("the domain :" , "[" ,minX,";",maxX,"]","[", minY,";",maxY ,"]")

#showing a 2D image of the topo
#plt.imshow(data, cmap='gist_earth',extent=[minx, maxx, miny, maxy])
#plt.show()

# elevation 2D numpy array
elevation = raster.ReadAsArray()

a = gt[1]
b = gt[2]
d = gt[4]
e = gt[5]

def pixelcoord(x, y):
  """Returns coordinates X Y from pixel"""
  xp = a * x + b * y + minX
  yp = d * x + e * y + minY
  return xp, yp
#25.01485910728215
#"creating X Y Z file..."
for i in range(height):
  for j in range(width):
     pp= pixelcoord(i,j)
     # if elevation[i][j] != -32767:
     print(pp[0] , pp[1] , elevation[i][j])