import requests
from bs4 import BeautifulSoup
import pandas

base_url="http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

l=[] #list of propoerties, each property corresponds to a dictionnary
for page in range(0,30,10):
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})

    for item in all:
        d={}
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            d["SquareFoot"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["SquareFoot"]=None
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None
        try:
            d["FullBaths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["FullBaths"]=None
        try:
            d["Halfbaths"]=item.find("span",{"class":infoValueHalfBath}).find("b").text
        except:
            d["HalfBaths"]=None
        l.append(d)
        
df=pandas.DataFrame(l)

df.to_csv('output.csv', sep=';')
