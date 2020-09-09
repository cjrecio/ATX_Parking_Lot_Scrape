#!/usr/bin/env python
# coding: utf-8

# In[24]:


from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as BSoup

my_url = 'https://www.bestparking.com/austin-tx-parking-2/'

#opening connection and getting page
u_Client = urlReq(my_url)
page_html = u_Client.read()
u_Client.close()

#parsing
page_soup = BSoup(page_html, 'html.parser')

#takes all parking lots
containers = page_soup.findAll('div', {'class': 'listing-container row'}) 

#opens spreadsheet
filename = "parking.csv"
f = open(filename, "w")

headers = "garage_name, address, price\n"

f.write(headers)

for container in containers:
    garage_name = container.findAll("div", {"location-name"})
    garage = garage_name[0].text
    
    address_name = container.findAll("div", {"address"})
    addy = address_name[0].text
    
    price = container.findAll("div", {"listing-price text-align-right"})
    price_name = price[0].text
    
    print("Garage Name:" + str(garage))
    print("Address: " + str(addy))
    print("Price: " + str(price_name))
    
    f.write(garage + "," + addy + "," + price_name + "\n")

f.close()
    


# In[ ]:





# In[ ]:




