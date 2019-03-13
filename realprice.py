import pandas as pd
import shutil, pathlib, os, glob,csv
import matplotlib.pyplot as plt
import numpy             as np
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model

area   = ['中西區', '北區', '東區','永康區']
status = ['土地', '房地(土地+建物)+車位', '房地(土地+建物)']
dir    = os.path.dirname(os.path.realpath(__file__))

# merge.csv
file = os.path.join(dir,'merge.csv') 

# 初始化建立一個CSV，並賦予標頭。        
def init():
    index = r'鄉鎮市區,交易標的,土地區段位置/建物區段門牌,土地移轉總面積(平方公尺),都市土地使用分區,非都市土地使用分區,非都市土地使用編定,交易年月日,交易筆棟數,移轉層次,總樓層數,建物型態,主要用途,主要建材,建築完成年月,建物移轉總面積(平方公尺),建物現況格局-房,建物現況格局-廳,建物現況格局-衛,建物現況格局-隔間,有無管理組織,總價(元),單價(元/平方公尺),車位類別,車位移轉總面積(平方公尺),車位總價(元),備註,編號'
    with open(file, 'a') as init:
        init.write(index)
        
# 產製合併之CSV output.csv
def merge():   
    for item in os.listdir(dir):
        if os.path.isdir(os.path.join(dir,item)):
            path = os.path.join(dir,item)
            os.chdir(path)
            
            for file in glob.glob("D_lvr_land_A.csv"):
                target = os.path.join(path,file)
                
                # 好像不必要正規化檔名
                # os.rename(target,  item + '.csv') 
                # file_list.append(target)    
 
                if item[:3] != '107':
                    print("Dealing with : ",target)
                    with open(target, errors = 'ignore', encoding='big5') as f:
                        for i in f:
                            if i[:3] in area:
                                add_to_csv(i)
                            elif i[:2] in area: 
                                add_to_csv(i)
                elif item[:3] == '107':
                    print("Dealing with : ",target)
                    with open(target, errors = 'ignore', encoding='utf8') as f:
                        for i in f:
                            if i[:3] in area:
                                add_to_csv(i)
                            elif i[:2] in area: 
                                add_to_csv(i)

# 新增自csv                                
def add_to_csv(content):
    with open(file,'a') as f:
        f.write(content)
        f.close()        

# 讀取merge.csv，拿掉不要的欄位，空的欄位用nah填滿然後都刪掉(去除無效的列)
def step_1(name):
    s1 = os.path.join(dir, name)
    con_1 = ['鄉鎮市區','交易標的','土地移轉總面積(平方公尺)','建物型態','交易年月日','建物移轉總面積(平方公尺)','總價(元)','單價(元/平方公尺)']
    con_2 = ['交易年月日','鄉鎮市區','交易標的','單價(元/平方公尺)']
    df = pd.read_csv(file,encoding='big5')
    df = df[con_2]

    # 去除無效的列
    df['單價(元/平方公尺)'].replace('', np.nan, inplace=True)
    df.dropna(subset=['單價(元/平方公尺)'], inplace=True)

    open(s1,'w')
    df.to_csv(s1, encoding='big5')
    return s1
    
# 區域各自合併(北、中西、東) + 土地、房地(土地+建物)、房地(土地+建物)+車位
# name = 輸出名稱, area = 區域, status = 土地或有無車位
def step_2(src_file ,name, area, status):   
    con_2 = ['交易年月日','鄉鎮市區','交易標的','單價(元/平方公尺)']
    s2 = os.path.join(dir,name)
    open(s2,'a')
    df = pd.read_csv(src_file, encoding='big5')          
    north     = df.loc[(df['鄉鎮市區'] == area  ) & (df['交易標的'] == status)].to_csv(os.path.join(dir,name   ), columns=con_2, encoding='big5', index=False)
    #east      = df.loc[(df['鄉鎮市區'] == '東區'  ) & (df['交易標的'] == '房地(土地+建物)+車位')].to_csv(os.path.join(dir,'east.csv'    ), columns=con_2, encoding='big5', index=False)
    #midwest   = df.loc[(df['鄉鎮市區'] == '中西區') & (df['交易標的'] == '房地(土地+建物)+車位')].to_csv(os.path.join(dir,'midwest.csv' ), columns=con_2, encoding='big5', index=False)
    return s2

# 忘了...    
def get_df(name):
    total_list = []
    need = ['交易年月日','單價(元/平方公尺)']
    s3   = os.path.join(dir, name)
    df = pd.read_csv(s3, encoding='big5')[need]
    df['交易年月日'] = df['交易年月日']//10000
    df['單價(元/平方公尺)'] = df['單價(元/平方公尺)']*10/3/10000
    df = df.dropna(axis=0,how='all')  
    df = df.dropna(axis=1,how='all')
    df = df.apply(lambda x: pd.to_numeric(x,errors='ignore')) 
    return df
    
# 有幾筆交易
def get_total(name):
    total_list = []
    need = ['交易年月日','單價(元/平方公尺)']
    s3   = os.path.join(dir, name)
    df = pd.read_csv(s3, encoding='big5')[need]
    df['交易年月日'] = df['交易年月日']//10000
    df['單價(元/平方公尺)'] = df['單價(元/平方公尺)']*10/3/10000

    total_102  = total_list.append(len(df.loc[(df['交易年月日'] == 102)].index))
    total_103  = total_list.append(len(df.loc[(df['交易年月日'] == 103)].index))
    total_104  = total_list.append(len(df.loc[(df['交易年月日'] == 104)].index))
    total_105  = total_list.append(len(df.loc[(df['交易年月日'] == 105)].index))
    total_106  = total_list.append(len(df.loc[(df['交易年月日'] == 106)].index))
    total_107  = total_list.append(len(df.loc[(df['交易年月日'] == 107)].index))
    return total_list

# 平均價格    
def get_mean(name):
    mean_list = []
    need = ['交易年月日','單價(元/平方公尺)']
    s3   = os.path.join(dir, name)
    df = pd.read_csv(s3, encoding='big5')[need]
    df['交易年月日'] = df['交易年月日']//10000
    df['單價(元/平方公尺)'] = df['單價(元/平方公尺)']*10/3/10000
    # df.plot(title=name[:-4]+' scatter',kind='scatter', x='交易年月日' , y='單價(元/平方公尺)', marker='.')
    # plt.show()
    # df.mean().plot(kind='bar')
    # plt.show()
    # price_104  = df.loc[(df['交易年月日'] == 104)]
    # price_105  = df.loc[(df['交易年月日'] == 105)]
    # price_106  = df.loc[(df['交易年月日'] == 106)]
    price_102 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 102)]['單價(元/平方公尺)'].mean()))
    price_103 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 103)]['單價(元/平方公尺)'].mean()))
    price_104 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 104)]['單價(元/平方公尺)'].mean()))
    price_105 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 105)]['單價(元/平方公尺)'].mean()))
    price_106 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 106)]['單價(元/平方公尺)'].mean()))   
    price_107 = mean_list.append(float('%.2f' % df.loc[(df['交易年月日'] == 107)]['單價(元/平方公尺)'].mean()))   
     
    return mean_list

# 畫圖
def plot(index, data, label):
    plt.plot(index, data  , label = label, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend(loc='best')
    plt.xticks(index)
    plt.ylim((10, 25))

# 機器學習(LinearRegression)
def linearRe(df):
    from sklearn                  import datasets, linear_model
    from sklearn.preprocessing    import PolynomialFeatures
    from sklearn.cross_validation import train_test_split
    from sklearn.preprocessing    import StandardScaler
    
    regr        = linear_model.LinearRegression()
    
    quadratic = PolynomialFeatures(degree=2)

    # df = df[['交易年月日']]
    df = df[df['單價(元/平方公尺)']<50]
    x = df[['交易年月日']]
    y = df[['單價(元/平方公尺)']]

    # 切分訓練及測試資料
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3) # 30% for testing, 70% for training

    x_train_raw = x_train.copy()
    x_test_raw  = x_test.copy()
    
    # 產生二次項係數
    x_train     = quadratic.fit_transform(x_train_raw)
    x_test      = quadratic.fit_transform(x_test_raw)
    x_fit       = pd.DataFrame(np.arange(100, 108, 1))
    
    # 訓練
    regr.fit(x_train, y_train)
    
    print("各變項參數: \n", regr.coef_)
    print("均方誤差 (Mean squared error, MSE): %.2f" % np.mean((regr.predict(x_test) - y_test) ** 2))

    

    plt.scatter(x_test_raw, y_test,  color='blue', marker = 'x')
    plt.plot(x_fit, regr.predict(quadratic.fit_transform(x_fit)), color='green', linewidth=1)
    plt.show()
    
def main():
    index = [102, 103 , 104, 105, 106, 107]
    label = ['north.csv','midwset.csv','east.csv','yongkong.csv']

    # init()
    # merge()  
    
    # linearRe(get_df('east.csv'))
    # linearRe(get_df('midwest.csv'))
    # linearRe(get_df('north.csv'))
    
    # 有車位
    north_y     = get_mean(step_2(step_1('select_col.csv'),'north.csv'     , area[0], status[1]))
    east_y      = get_mean(step_2(step_1('select_col.csv'),'east.csv'      , area[1], status[1]))
    midwest_y   = get_mean(step_2(step_1('select_col.csv'),'midwest.csv'   , area[2], status[1]))
    youngkong_y = get_mean(step_2(step_1('select_col.csv'),'yongkong.csv'  , area[3], status[1]))
    
    # 無車位
    north_n     = get_mean(step_2(step_1('select_col.csv'), 'north.csv'    , area[0], status[2]))  
    east_n      = get_mean(step_2(step_1('select_col.csv'), 'east.csv'     , area[1], status[2]))
    midwest_n   = get_mean(step_2(step_1('select_col.csv'), 'midwest.csv'  , area[2], status[2]))
    youngkong_n = get_mean(step_2(step_1('select_col.csv'), 'yongkong.csv' , area[3], status[2]))   
    
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plot(index, north_y    , label=label[0][0:-4])
    plot(index, east_y     , label=label[1][0:-4])
    plot(index, midwest_y  , label=label[2][0:-4])
    plot(index, youngkong_y, label=label[3][0:-4])
    plt.title('Have Parking space')
    
    plt.subplot(1, 3, 2)
    plot(index, north_n    , label=label[0][0:-4])
    plot(index, east_n     , label=label[1][0:-4])
    plot(index, midwest_n  , label=label[2][0:-4])
    plot(index, youngkong_n, label=label[3][0:-4])
    plt.title('No Parking space')
    
    plt.subplot(1, 3, 3)
    plt.plot(index, get_total('north.csv'  )   , label = 'north', marker='o')
    for a, b in zip(index, get_total('north.csv'  )):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    
    plt.plot(index, get_total('midwest.csv')   , label = 'midwest', marker='o')
    for a, b in zip(index, get_total('midwest.csv'  )):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.plot(index, get_total('east.csv'   )   , label = 'east', marker='o')
    for a, b in zip(index, get_total('east.csv'  )):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
   
    plt.plot(index, get_total('yongkong.csv'   )   , label = 'youngkong', marker='o')
    for a, b in zip(index, get_total('yongkong.csv'  )):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    
    plt.xlabel('Year')
    plt.ylabel('count')
    plt.grid(True)
    plt.legend(loc='best')
    plt.title('Turnover volume(accumulated to 107/06)')
    plt.xticks(index)

    plt.show()
        
main()