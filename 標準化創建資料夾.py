import pathlib

name = input()

pathlib.Path('./'+ name).mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/2.環景照片').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/3.一般產品').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/4.影片').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/Photoscan').mkdir(parents=True, exist_ok=0)
open('.\\'+ name + '\\Photoscan' + '\\' + name + '.psx','w')
pathlib.Path('./'+ name + '/1.測繪產品' + './1.1.Ortho_正射影像(包含附加檔)').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.2.OrigPhoto_原始照片').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.3.PrecEval_精度評估報告').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.4.ContCoor_控制點座標)').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.5.ContPhoto_控制點照片').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.6.FlyRec_飛行記錄').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.7.DSM_數值地表模型').mkdir(parents=True, exist_ok=0)
pathlib.Path('./'+ name + '/1.測繪產品' + './1.8.3DModel_3D模型').mkdir(parents=True, exist_ok=0)



