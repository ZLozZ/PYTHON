from bs4 import BeautifulSoup
import requests
import numpy as np

j = 0
file_= open('cau1.txt','w',encoding='utf-8')
web = requests.get('https://zingnews.vn/cong-nghe.html').text
soup = BeautifulSoup(web)

phandau=soup.find('div',class_='article-list listing-layout responsive infinite-load')
phanthan=phandau.find_all('article',class_='article-item')


for i in phanthan:
    j+=1
    dulieu = i.find('header')
    title = dulieu.find('a').text.replace('  ','').replace('\n','')
    tomtat= dulieu.find('p',class_="article-summary").text.replace('  ','').replace('\n','')
    thoigian = i.find('span',class_="time").text + " " + i.find('span',class_="date").text

    link1 = i.find('p',class_="article-thumbnail")
    link = 'https://zingnews.vn/cong-nghe.html' + link1.find('a')['href']
    file_2=('- Tittel: {}\n + describe : {}\n + Time: {}\n + Link:{}\n\n'.format(title,tomtat,thoigian,link))
    print(file_2)
    file_.write(str(file_2))
    if (j==5):
        break
file_.close()