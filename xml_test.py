import requests 
import xml.etree.ElementTree as ET
from xml.dom import minidom


path = r'C:\Users\RSLAB\Desktop\\'


dic_1 = {
            "text" : "山坡地地籍圖",
            "id"   : "23.549765;121.113281",
            "pos"  : "http://140.116.228.176/vectortiles/tcgeo/shp/TCSHP001/"
         }
         
dic_3D_1 = {
            "text"  : "臺北市北投區秀山段三小段北投22號公園新建工程_3D",
            "lt"    : "25.145432;121.492619",
            "date"  : "20180522",
            "othro" : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/",
            "cad"   : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/dwg.kml",
            "model" : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/"
           }

dic_3D_2 = {
            "text"  : "臺北市北投區崇仰段二小段202地號土原有合法建築物整建及增建臨時建築工程_3D",
            "lt"    : "25.128703;121.508834",
            "date"  : "20180522",
            "othro" : "https://geodac.ncku.edu.tw/TCGEO/20180523_臺北市北投區崇仰段二小段202地號土原有合法建築物整建及增建臨時建築工程/",
            "cad"   : "https://geodac.ncku.edu.tw/TCGEO/20180523_臺北市北投區崇仰段二小段202地號土原有合法建築物整建及增建臨時建築工程/北投區崇仰段.kml",
            "model" : "https://geodac.ncku.edu.tw/TCGEO/20180523_臺北市北投區崇仰段二小段202地號土原有合法建築物整建及增建臨時建築工程/臺北市北投區崇仰段二小段202地號土原有合法建築物整建及增建臨時建築工程_3D圖磚/"
           }
           
           
dic_2D_1 = {
            "text"  : "臺北市北投區秀山段三小段北投22號公園新建工程_3D",
            "lt"    : "25.145432;121.492619",
            "date"  : "20180522",
            "cad"   : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/dwg.kml",
            "othro1" : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/"
            }
            
dic_2D_2 = {
            "text"  : "臺北市內湖區康寧段一小段312地號住宅新建工程",
            "lt"    : " 25.082980,121.600714",
            "date"  : "20180625",
            "cad"   : "https://geodac.ncku.edu.tw/TCGEO/20180522_BeitouPark_Tile/dwg.kml",
            "othro" : "https://geodac.ncku.edu.tw/TCGEO/20180626_臺北市內湖區康寧段一小段312地號住宅新建工程/"
            }
           
root = ET.Element('tree',id="0")

dic = dic_1
ET.SubElement(root, "item", text=dic['text'] ,id=dic['id'] + r";696480;8@MVTTile@" + dic['pos'], im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif").text = None


dic = dic_3D_1

def add_3D(dic):
    one = ET.SubElement(root, "item", text=dic['text'], id=dic['text'], nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
    check(dic['othro']+'index.html')
    check(dic['cad'])
    check(dic['model']+'tileset.json')
    ET.SubElement(one , "item", text = '正射影像_' + dic['date'] + '(雙擊定位)',  id=dic['lt']+';;18@TileImage_ps@'+dic['othro'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    ET.SubElement(one , "item", text = '工程圖說'                              ,  id=dic['lt']+';;18@kml@'      +dic['cad']  ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    ET.SubElement(one , "item", text = '3D_模型'                               ,  id=dic['lt']+';;18@3DModel@'  +dic['model'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    #ET.SubElement(one , "item", text = '正射影像_' + dic['date'] + '(雙擊定位)',  id=dic['lt']+';;18@TileImage@'+dic['othro'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    #ET.SubElement(one , "item", text = '工程圖說'                              ,  id=dic['lt']+';;18@kml@'      +dic['cad']  ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    return 0

def add_2D(dic):
    one = ET.SubElement(root, "item", text=dic['text'], id=dic['text'], nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
    check(dic['othro']+'index.html')
    #check(dic['cad']) 
    ET.SubElement(root  , "item", text = '正射影像_' + dic['date'] + '(雙擊定位)',  id=dic['lt']+';;18@TileImage+ps@'+dic['othro'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    #ET.SubElement(one  , "item", text = '工程圖說'                              ,  id=dic['lt']+';;18@kml@'      +dic['cad']  ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
    return 0

      
    
def pprint(x):
    xmlstr = minidom.parseString(x).toprettyxml(indent="   ")
    print(xmlstr)

def output_xml(x):
    xmlstr = minidom.parseString(x).toprettyxml(indent="   ")
    with open(path  + "output.xml", "a") as f:
        f.write(xmlstr)
    print('輸出完成!')
    
def check(url):
    res = requests.get(url)
    if   res.status_code == 200:
        print(url, ' -> 圖資在線!')
    else:
        print('請確認圖資是否掛載:',url)
        
def main():

    add_2D(dic_2D_2)
    #add_3D(dic_3D_2)
    output_xml(ET.tostring(root))
    pprint(ET.tostring(root))

main()

    
    
    
    
    
    
    
    

# one = ET.SubElement(root, "item", text=dic['text'], id=dic['text'], nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
# ET.SubElement(one , "item", text = '正射影像_' + dic['date'] + '(雙擊定位)',  id=dic['lt']+';;18@TileImage@'+dic['othro'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
# ET.SubElement(one , "item", text = '工程圖說'                              ,  id=dic['lt']+';;18@kml@'      +dic['cad']  ,  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
# ET.SubElement(one , "item", text = '3D_模型'                               ,  id=dic['lt']+';;18@3DModel@'  +dic['model'],  im0='hd.gif',  im1='folderOpen.gif',  im2='folderClosed.gif').text = ' '
