import requests 
from bs4 import BeautifulSoup
import pandas as pd
import csv

def getdata():
    examplefile = open('paste here path of your csv file containing URLS')
    exreader = csv.reader(examplefile)
    exedata=list(exreader)
    newurllist = []
    productname=[]
    pricelist=[]
    ratinglist=[]
    for newurls in exedata:
        newurllist.append(newurls[0])
    for url in newurllist:
        checkurl= url.split("/")
        r=requests.get(url)
        if checkurl[2] == "www.flipkart.com":
            soup =BeautifulSoup(r.content)
            data =soup.find_all('a',href=True, attrs={'class':'_31qSD5'})
            for a in data:
                name = a.find('div' ,attrs={'class':'_3wU53n'})
                price = a.find('div' ,attrs={'class':'_1vC4OE'})
                rating =a.find('div' ,attrs={'class':'hGSR34'})
                productname.append(name.text)
                pricelist.append(price.text)
                ratinglist.append(rating.text)
                #similarly can be done for various web sites.
        # if checkurl[2] == "www.snapdeal.com":
        #     print("in snapdeal")
        #     soup =BeautifulSoup(r.content)
        #     data2 =soup.find_all('div',href=True, attrs={'class':'dp-widget-link noUdLine hashAdded'}) 
        #     for i in data2:
        #         name1 = i.find('span' ,attrs={'class':'product-title '})
        #         price2 = i.find('span' ,attrs={'class':'lfloat product-price'})
        #         rating3 =i.find('span' ,attrs={'class':'avrg-rating'})
        #         productname.append(name1.text)
        #         pricelist.append(price2.text)
        #         ratinglist.append(rating3.text)    


    df =pd.DataFrame({'Product Name':productname,'Price':pricelist,'Rating':ratinglist})
        # print(df)
    df.to_csv('C:/Users/CS-10/Desktop/products.csv', index=False, encoding='utf-8')


getdata()




