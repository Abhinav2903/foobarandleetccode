from urllib.request import Request,urlopen as uReq
from bs4 import BeautifulSoup as soup
#url string
my_url="https://www.newegg.com/Cell-Phones/Category/ID-450"
#here we have chnaged url with useragent as sometime the webpage gives error
#so we provided pseudo agent mozilla
#req=Request(my_url,headers={'User-Agent': 'Mozilla'})
uClient=uReq(my_url)

#read page or url
#page_byte=uClient.read()
#page_html=page_byte.decode('utf-8')
page_html=uClient.read()

#close the connection
uClient.close()
#html parsing
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"item-container"})
#container=containers[0]

# here we create  a new file for our csv data
filename = "product.csv"
f=open(filename,"w")
headers="Brand,ProductName,OperatingSystem,Price,Shipping\n"
f.write(headers)

#for loop for looping our the containers and extraction of deaired data 
for container in containers:
    brand_container=container.findAll("a",{"class":"item-brand"})
    if(brand_container):
        Brand=brand_container[0].img["title"].strip()
    else:
        Brand=container.a.img["title"][0:8]    
    ItemName=container.a.img["title"]
    
    feature_container=container.findAll("ul",{"class":"item-features"})
    OperatingSystem=feature_container[0].li.text[18:].strip()
    
    price_container=container.findAll("li",{"class":"price-current"})
    Price=price_container[0].strong.text
    
    ship_conatiner=container.findAll("li",{"class":"price-ship"})
    Shipping=ship_conatiner[0].text.strip()
    
    print("Brand     :"+Brand)
    print("Item Name :"+ItemName)
    print("Operating System:"+OperatingSystem)
    print("Price     :"+"$"+Price)
    print("Shipping  :"+Shipping+"\n")
    
    #writing the data in the file  
    f.write(Brand+","+ItemName+","+OperatingSystem+","+"$"+Price.replace(",","")+","+Shipping+"\n")

f.close()