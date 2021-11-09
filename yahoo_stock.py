import requests
from bs4 import BeautifulSoup
import pandas as pd

def name_price(url):
    resp=requests.get(url)
    
    #print(resp) response 200代表連接成功
    #print(resp.text) 以文字檔形式呈現網頁原代碼
    
    html=resp.content.decode("utf-8")
    #print(html) 解碼之後列印整張網頁
    
    soup=BeautifulSoup(html,"html.parser")
    #print(soup)
    
    div_names=soup.find_all("div","span",class_="Lh(20px) Fw(600) Fz(16px) Ell")
    div_prices=soup.find_all("div","span",class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(90px)")
    #print(div_names)
    
    stocks_name=[]
    for name in div_names:
        stock_name= name.text.split()
        #print(stock_name)
        stocks_name.append(stock_name)
    #print(stocks_name)
    #print(len(stocks_name))
    


    stocks_price=[]
    for price in div_prices[1:]:
        stock_price=price.text.split()
        stocks_price.append(stock_price)
    #print(stocks_price)
    #print(len(stocks_price))
    
    

    _data=pd.DataFrame()
    _data['company']=stocks_name
    _data['price']=stocks_price
    
    return _data
    


stock=name_price("https://tw.stock.yahoo.com/world-indices")
stock.to_csv('yahoo_stock',encoding='utf-8')
