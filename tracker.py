import requests
from bs4 import BeautifulSoup
import os
from datetime import date
import sys

vendor = ""
vendor_list = ["amz", "ebay", "zalando"]
if len(sys.argv) > 1:

    if sys.argv[1] in vendor_list:
        vendor = sys.argv[1]
    else:
        print(f"\n---The specified vendor must be among the following:{vendor_list}")
        exit(0)
else:
    print("\n ----You have not specified which vendor to use!----\n")
    exit(0)

with open('useragent.txt') as f:
    lines = [line.rstrip('\n') for line in f]
headers = {'User-Agent': lines[0]}

if vendor == "amz":
    fname = "amazon-"+'itemlist.txt'
elif vendor=="ebay":
    fname = "ebay-"+'itemlist.txt'
with open(f'./itemlist/{fname}') as f:
    lines = [line.rstrip('\n') for line in f]

if not lines:
    print(f"\n\n---The Item List for {vendor} is empty!---\n\n")
    exit(0)

for url in lines:
    if url != "": 
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')

            if vendor == "amz":
                title = soup.find(id='productTitle').get_text()
                subtitle = soup.find(id='productSubtitle').get_text()
                # info = soup.find(id='bylineInfo').get_text()
                price = soup.find("span", {'class':'a-size-base a-color-price a-color-price'}).get_text().strip().strip('€').replace(',','.')
                price = float(price) # easy way to remove a weird non-displayable character

            elif vendor == "ebay":
                title = soup.find("h1",{'class':'x-item-title__mainTitle'}).find("span", {'class':'ux-textspans ux-textspans--BOLD'}).get_text().strip()
                price = soup.find("span", {'itemprop': 'price'})['content']
                price = float(price)
                subtitle = "ebay"

            title = "".join(c for c in title if c.isalnum()) #remove all non alphanumeric
            subtitle="".join(c for c in subtitle if c.isalnum())
                
            
            print(f"- Found {title} {subtitle} {price} \n")
            
            fname = title + '-' + subtitle
            # fname = "".join(c for c in fname if c.isalnum())
            path = './tracked/'+ fname
            if os.path.exists(path):
                f = open(path, "a")
            else:
                f = open(path, 'w')
                f.write("date,price\n") # setup the csv if you're creating it

            f.write(str(date.today()) + ',' + str(price) + '\n')
            f.close()

        else:
            print("Page currently unavailable, url = " + url)