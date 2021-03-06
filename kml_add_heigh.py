import osr, os, affine, time
from gdalconst import *
from osgeo import gdal

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