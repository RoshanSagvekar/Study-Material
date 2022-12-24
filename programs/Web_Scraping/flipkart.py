import requests
from bs4 import BeautifulSoup
import pandas as pd

product_name = []
product_price = []
# accepts the number of pages for scraping data
page_num = int(input("Enter number of pages:"))

for i in range(1,page_num+1):
    url = "https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&page="+str(i)
    # requests to the server
    req = requests.get(url)
    # parse the content into html
    content = BeautifulSoup(req.content,"html.parser")
    name = content.find_all('div',{'class':"_4rR01T"})
    price = content.find_all('div',{'class': "_30jeq3 _1_WHN1"})
    # print("Phone in page "+str(i))
    # print(len(name))
    # print(len(price))

    # stores the data in the lists
    for i in name:
        product_name.append(i.text)

    for i in price:
        product_price.append(i.text)

# display data in table format
data = {"Product Name":product_name,"Price":product_price}
df = pd.DataFrame(data)
print(df)
print("THANK YOU !!!")


df.to_csv('products.csv',index=False,encoding='utf_8')