import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

data_fpt = []
data_thegioididong = []
data_viettel = []

#tgdd
drivertgdd = webdriver.Chrome('D:\\CODE\\Hoc_Python\B10\\chromedriver.exe')
drivertgdd.get('https://www.thegioididong.com/dtdd-apple-iphone')
sleep(3)
webthegioididong = drivertgdd.page_source 
soup_tgdd = BeautifulSoup( webthegioididong ,'html.parser')
datas = soup_tgdd.find_all('li', class_="item ajaxed __cate_42")
for data in datas:
    name =  data.find('a')['data-name']
    name = name[11:len(name)]
    price = data.find('strong',class_="price").text
    data_thegioididong.append({'Ten Iphone': name,'Gia Thegioididong': price})

#fpt
driverfpt = webdriver.Chrome('D:\\CODE\\Hoc_Python\B10\\chromedriver.exe')
driverfpt.get('https://fptshop.com.vn/dien-thoai/apple-iphone')
sleep(3)
webfpt = driverfpt.page_source
soup_fpt = BeautifulSoup(webfpt ,'html.parser')
for data in soup_fpt.find_all('div', class_="cdt-product product-sale"):
    name = data.find('a',class_= 'cdt-product__name').text
    price = data.find('div',class_= 'progress').text
    data_fpt.append({'Ten Iphone':name,'Gia FPT':price})


#viettle
drivervt = webdriver.Chrome('D:\\CODE\\Hoc_Python\B10\\chromedriver.exe')
drivervt.get('https://viettelstore.vn/dtdd-apple-iphone')
sleep(3)
webviettel = drivervt.page_source
soup_viettel = BeautifulSoup(webviettel, 'html.parser')
datas = soup_viettel.find_all('div', class_='item ProductList3Col_item')
for data in datas:
    name= data.find('h2', class_='name').text
    price = data.find('span',class_='price').text
    data_viettel.append({'Ten Iphone': name,'Gia ViettleStore':price})


ds1 = pd.DataFrame(data_thegioididong)
ds2 = pd.DataFrame(data_fpt)
ds3 = pd.DataFrame(data_viettel)
ds4 = pd.merge(ds1, ds2, how='outer')
ps = pd.merge(ds4, ds3, how = 'outer')
ds1 = pd.DataFrame(data_thegioididong)
ds2 = pd.DataFrame(data_fpt)
ds3 = pd.DataFrame(data_viettel)
ds4 = pd.merge(ds1, ds2, how='outer')
ps = pd.merge(ds4, ds3, how = 'outer')

result = []
STT = []
for i in range(0, len(ps)):
    STT.append(i)
STT = pd.DataFrame(STT)
result = pd.DataFrame(result)
result['STT'] = STT
ps1 = pd.merge(result, ps, left_index=True, right_index=True)
print(ps1)
ps1.to_csv('Result.csv', index = False)
