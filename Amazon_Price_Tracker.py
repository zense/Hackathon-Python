import requests
from bs4 import BeautifulSoup
from pushbullet import PushBullet
from threading import Timer


URL = 'https://www.amazon.in/Apple-iPhone-8-Gold-256GB/dp/B071P3764Z/ref=sr_1_2?crid=3REL7USFBYB3I&dchild=1&keywords=apple+i+phone7s+plus&qid=1616307855&sprefix=apple+i+p%2Caps%2C325&sr=8-2'
desired_price=50000
API_KEY = 'o.8UljdagUxLKUyT0IEhPHxKHSxHCYMo59'


headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}


def notification(product_name,product_price):

    text=product_name
    text+=' is now available for your desired price.'
    text+='\n You can get it now at '
    text+=product_price
    text+='\n'
    text+=URL
    
    pb=PushBullet(API_KEY)
    
    push = pb.push_note('Price Drop',text)

    print('Notification Sent!')


def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    product_name = soup.find(id='productTitle').get_text()
    product_name = str(product_name)
    product_name = product_name.strip()
    #print(product_name)

    a=soup.find(id='priceblock_dealprice')
    if(a==None):
        product_price1 = soup.find(id='priceblock_ourprice').get_text()
    else:
        product_price1 = soup.find(id='priceblock_dealprice').get_text()
    #print(product_price1)

    product_price =''
    for letters in product_price1:
        if letters.isnumeric() or letters =='.':
            product_price+=letters
    product_price=float(product_price)
    #print(product_price)

    if product_price<=desired_price:
        print("Price of the Product reached below the Desired Price.")
        notification(product_name,product_price1)
        return
    else:
        print("Price of the Product is still more than the Desired Price.")
    
    Timer(60*60,check_price).start()

check_price()


