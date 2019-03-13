import requests 
import xml.etree.ElementTree as ET
from xml.dom import minidom


path = r'C:\Users\RSLAB\Desktop\\'

mp_name = [ "20180606_桃園市龍潭區水土保持教室",
            "20180628_臺南市玉井區沙田水土保持教學教室",
            "20180628_臺南市龍崎區牛埔泥水土保持教學教室",
            "20180806_南投縣草屯鎮風水坪水土保持戶外教室",
            "20180806_雲林縣古坑鄉華山土石流教學園區",
            "20180807_嘉義市東區嘉義農業試驗分所",
            "20180823_桃園縣復興鄉",
            "20180823_新竹縣五峰鄉",
            "20180823_新竹縣尖石鄉梅花村",
            "20180920_南投縣水里鄉興隆村",
            "20180921_高雄市桃源區拉芙蘭里",
            "20181016_嘉義縣大埔鄉和平村",
            "20181030_高雄市那瑪夏區旗山溪",
            "20181018_苗栗縣三義鄉火炎山",
            "20181017_南投縣仁愛鄉慈峰部落",
            "20181009_基隆市暖暖區",
            "20181003_高雄市杉林區火山橋",
            "20180929_新北市樹林區寮里三角埔頂山",
            "20181012_南崗UAV校驗航拍"
          ]
            
lon = [
            "24.86628932;121.1680491",
            "23.122449;120.47852",
            "22.935189;120.4072",
            "23.9634083;120.7211198",
            "23.59619964;120.6033359",
            "23.47833218;120.4753854",
            "24.78377254;121.3562838",
            "24.64641565;121.1217118",
            "24.6735533;121.19984",
            "23.76833859;120.8526057",
            "23.23565651;120.8179758",
            "23.29806991;120.6093599",
            "23.28413894;120.7189404",
            "24.36210802;120.7295169",
            "24.1328559;121.1874733",
            "25.07812985;121.75127",
            "23.01264728;120.5753558",
            "25.00655488;121.4081587",
            "23.92826252;120.661636"
     ]

dir =[
            "/SWCB_LLGIS/3DModel/20180606_桃園市龍潭區水土保持教室/Batched20180606_桃園市龍潭區水土保持教室",
            "/SWCB_LLGIS/3DModel/20180628_臺南市玉井區沙田水土保持教學教室/Batched20180628_玉井區沙田水土保持教學教室",
            "/SWCB_LLGIS/3DModel/20180628_臺南市龍崎區牛埔泥水土保持教學教室/Batched20180628_龍崎區牛埔泥水土保持教學教室",
            "/SWCB_LLGIS/3DModel/20180806_南投縣草屯鎮風水坪水土保持戶外教室",
            "/SWCB_LLGIS/3DModel/20180806_雲林縣古坑鄉華山土石流教學園區",
            "/SWCB_LLGIS/3DModel/20180807_嘉義市東區嘉義農業試驗分所",
            "/SWCB_LLGIS/3DModel/20180823_桃園縣復興鄉",
            "/SWCB_LLGIS/3DModel/20180823_新竹縣五峰鄉/Batched20180823_新竹縣五峰鄉_v2",
            "/SWCB_LLGIS/3DModel/20180823_新竹縣尖石鄉梅花村/Batched20180823_新竹縣尖石鄉梅花村_v2",
            "/SWCB_LLGIS/3DModel/20180920_南投縣水里鄉興隆村/Batched20180920_南投縣水里鄉興隆村_v2",
            "/SWCB_LLGIS/3DModel/20180921_高雄市桃源區拉芙蘭里/Batched20180921_高雄市桃源區拉芙蘭里_v2",
            "/SWCB_LLGIS/3DModel/20181016_嘉義縣大埔鄉和平村/Batchedmodel",
            "/SWCB_LLGIS/3DModel/20181030_高雄市那瑪夏區旗山溪/Batchedmodel",
            "/SWCB_LLGIS/3DModel/20181018_苗栗縣三義鄉火炎山/Batchedmodel",
            "/SWCB_LLGIS/3DModel/20181017_南投縣仁愛鄉慈峰部落/Batchedmodel",
            "/SWCB_LLGIS/3DModel/20181009_基隆市暖暖區/Batched20181009_基隆市暖暖區",
            "/SWCB_LLGIS/3DModel/20181003_高雄市杉林區火山橋/Batched20181003_高雄市杉林區火山橋_v2",
            "/SWCB_LLGIS/3DModel/20180929_新北市樹林區寮里三角埔頂山/Batched20180929_新北市樹林區?寮里三角埔頂山_v2",
            "/SWCB_LLGIS/3DModel/20181012_南崗UAV校驗航拍/Batched20181012_南崗UAV校驗航拍"
     ]
     
# id = cnter+front+dir
front = ";;18@3DModel@https://geodac.ncku.edu.tw"
     
id= []
output = []

for i in range(0,len(dir)):
    item = lon[i]+front+dir[i]+'/'
    #print(i,'\t',item)
    id.append(item)  



# init
root = ET.Element('tree',id="0")

   
def add_out(name,id):
    #one = ET.SubElement(root, "item", text=name, id=id, nocheckbox="1", im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif")
    
    for i in range(0,len(name)):
        print(id[i])
        ET.SubElement(root, "item", text=name[i] ,id=id[i], im0="hd.gif", im1="folderOpen.gif", im2="folderClosed.gif").text = None
        
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    
    with open(path  + "output.xml", "w") as f:
        f.write(xmlstr)   

    
  
    


add_out(mp_name,id) 
  
    
    
    
    
    