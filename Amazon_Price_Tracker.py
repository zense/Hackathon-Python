#Importing modules
import requests
from bs4 import BeautifulSoup
from pushbullet import PushBullet
from threading import Timer

URL = 'https://www.amazon.in/New-Apple-iPhone-Pro-128GB/dp/B08L5VZKWT/ref=sr_1_3?dchild=1&keywords=iphone&qid=1616338851&sr=8-3'
                                #URL of the product page(On Amazon)
desired_price=130000             #Price below which you should be notified
API_KEY = 'o.8UljdagUxLKUyT0IEhPHxKHSxHCYMo59'  #Access Token from pushbullet
interval=1                      #Enter value in hours(If interval=2 the program checks the price every 2 hours)


headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}
                                                #Web Scraping



def notification(product_name,product_price):   #Function which is used to send notification on our phone

    text=product_name
    text+=' is now available for your desired price.'
    text+='\n You can get it now at '
    text+=product_price
    text+='\n'
    text+=URL                                   #Text contains the message which will be displayed as notification
    
    pb=PushBullet(API_KEY)                      #Class Variable of API_KEY
    
    push = pb.push_note('Price Drop',text)      #Sending Notification
                                                #Title of Notification followed by text inside the parenthesis

    print('Notification Sent!')                 #Prints 'Notification Sent' on your terminal


def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    product_name = soup.find(id='productTitle').get_text()  #Finds id called productTitle which contains
                                                            #the name of the product on Amazon Page
    product_name = str(product_name)                        #Converts it into text
    product_name = product_name.strip()                     #It has a lot of extra spaces so removing them
    #print(product_name)


#In some pages price of the product is stored in id='priceblock_ourprice' and in some it is stored in id='priceblock_dealprice'
#So taking care of both
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
                                        #Price contains the rupee symbol so removing that and making it a float

    #print(product_price)

    if product_price<=desired_price:    
        print("Price of the Product reached below the Desired Price.")
        notification(product_name,product_price1)
        return
    else:
        print("Price of the Product is still more than the Desired Price.")
                                        #This blocks compares the price and calls the notification function if necessary
    
    Timer(interval*60*60,check_price).start()
                                        #This statement controls the time after which loop is run again
                                        #That is the time gap after which we should check the price

check_price()
