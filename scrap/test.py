from itertools import product
from re import T
import xlsxwriter
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
# import pandas as pd

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html,'html.parser')
# print(soup)

d=soup.body.find_all('div',attrs={'class': 's-item__info clearfix'})
workbook = xlsxwriter.Workbook('Book.xlsx')
worksheet = workbook.add_worksheet()

r=1
for i in d:
    k=i.find_all('h3',attrs={'class': 's-item__title'})
    k2=i.find_all('span',attrs={'class': 's-item__price'})
    k3=i.find_all('span',attrs={'class': 's-item__shipping s-item__logisticsCost'})  
    for a in k:
        worksheet.write(r,0,str(a.text))
    for s in k2:
        worksheet.write(r,1,str(s.text))
    for v in k3:
        worksheet.write(r,2,str(v.text))
    r=r+1
workbook.close()
