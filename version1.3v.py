from bs4 import BeautifulSoup as btu 
import requests as req 
import time 
import os


dosya = open("useragnet.txt","r+")
for usr in dosya.readlines():
    user = usr
    str(user)
    
    
url = "https://www.binance.com/en/markets"
istek = req.get( url, headers={f"User-Agent":"{user}"} )
html = istek.content
soup = btu(html, "lxml")







takma_ad=[]
for elem in soup.find_all("div", {"class":"css-1wp9rgv"}):
    takma_ad.append(elem.text)






genel_ad = []
for ele in  soup.find_all("div", {"class":"css-1ap5wc6"}):
    genel_ad.append(ele.text)







fiyati = []
for el in soup.find_all("div",{"class":"css-ovtrou"}):
    fiyati.append(el.text)







dusus_yukselis= []
for e in soup.find_all("div",{"class":"css-1ca67uc"}):
    dusus_yukselis.append(e.text)


# 






#




piyasa_deger = []
for la in soup.find_all("div", {"class":"css-s779xv"}):
    piyasa_deger.append(la.text)







def main():
    print("""
    Crypto Takma Adı:{}
    Crypto Genel adı:{}
    Crypto Fiyati:{}
    Crypto 24 saatlik değişim:{}
    Crypto Piyasa değeri:{}
    """.format(takma_ad[0],genel_ad[0],fiyati[0],dusus_yukselis[0],piyasa_deger[0]))


while True:
    main()
    time.sleep(8)
    os.system("clear")
    