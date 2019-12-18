import osr, os, affine, time
from gdalconst import *
from osgeo import gdal

def path_join(str):
    py_path    = os.path.dirname(os.path.realpath(__file__))
    abs_path = os.path.join(py_path,str) 
    if os.path.isfile(abs_path):
        return abs_path 
    else:
        print('[Alarm] File not exist:{}\n'.format(abs_path ))
        return abs_path 


def retrieve_pixel_value(geo_coord, data_source):
    """Return floating-point value that corresponds to given point."""
    x, y = geo_coord[0], geo_coord[1]
    forward_transform =  affine.Affine.from_gdal(*data_source.GetGeoTransform())
    reverse_transform =  ~forward_transform
    px, py = reverse_transform * (x, y)
    px, py = int(px + 0.5), int(py + 0.5)
    pixel_coord = px, py
    data_array = np.array(data_source.GetRasterBand(1).ReadAsArray())
    # i = data_array[0]
    # j = data_array[1]
    return(data_array[pixel_coord[1]][pixel_coord[0]])

    
# retuen lon list and lat list from kml file
def get_lon_lat(file_in, file_out, data):
    kml = []   
    with open(file_in, 'r', encoding='utf8') as origin:
        with open(file_out, 'w', encoding='utf8') as out:
            num = 0
            for line in origin.readlines():  
                if num == 1 :
                    out.write('\t\t\t\t\t\t\t')
                    for j in line.split():
                            if j != '</LineString>':
                                xlon = float(j.split(',')[0])
                                xlat = float(j.split(',')[1])
                                print(xlon, xlat)
                                h    = str(retrieve_pixel_value((xlon, xlat), data)+0.7)        
                                out.write(j.split(',')[0] + ',' + j.split(',')[1] + ',' + h + ' ')  
                                kml.append(j.split(',')[0] + ',' + j.split(',')[1] + ',' + h + '\n')
                    out.write('</LineString>')
                    num = 0
                else:                   
                    out.write(line) 
                
                if line.find('<coordinates>') > 0:
                    num = 1
    print('[OK] write kml.\n')
    return kml

def pixelcoord(x, y):
    """Returns coordinates X Y from pixel"""
    xp = a * x + b * y + minX
    yp = d * x + e * y + minY
    return xp, yp

def print_dem_value(file):
    data = gdal.Open(file, GA_ReadOnly)
    raster  = data.GetRasterBand(1)
    width   = data.RasterXSize
    height  = data.RasterYSize
    gt      = data.GetGeoTransform()
    minX = gt[0]
    minY = gt[3] + width*gt[4] + height*gt[5] 
    maxX = gt[0] + width*gt[1] + height*gt[2]
    maxY = gt[3] 

    # print ("the domain :" , "[" ,minX,";",maxX,"]","[", minY,";",maxY ,"]")

    # showing a 2D image of the topo
    # plt.imshow(data, cmap='gist_earth',extent=[minx, maxx, miny, maxy])
    # plt.show()

    # elevation 2D numpy array
    elevation = raster.ReadAsArray()

    a = gt[1]
    b = gt[2]
    d = gt[4]
    e = gt[5]  
      
    for i in range(height):
      for j in range(width):
         xp = a * i + b * j + minX
         yp = d * i + e * j + minY
         if elevation[i][j] != -32767:
            print(xp , yp, elevation[i][j])

def write_it(file, list):
    with open(file, 'w') as f:
        for line in list:          
            f.write(line)
    

def main():    
    start_time = time.time()   
    # kml_file   = path_join('t.kml')
    # kml_out    = path_join('kml_add.kml')
    # dem_file   = path_join('dem_410_wgs84.tif')
    # test_file  = path_join('test.txt')
    
    f = r'C:\Users\RSLAB\Desktop\臺北市北投區行義段一小段506等\20190314_臺北市北投區行義段一小段506、507、509、510、511、514地號等六筆土地宗祠新建工程水土保持計畫_wgs84.tif'
    k0 = r'C:\Users\RSLAB\Desktop\臺北市北投區行義段一小段506等\doc.kml'
    k1 = r'C:\Users\RSLAB\Desktop\臺北市北投區行義段一小段506等\add_doc.kml'

    # print_dem_value(dem_file)
    data  = gdal.Open(f, GA_ReadOnly)
    array = get_lon_lat(k0, k1, data)
    # write_it(test_file, array)
    
        
    print("--- %s seconds ---" % (time.time() - start_time))
    
main()