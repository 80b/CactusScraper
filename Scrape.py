from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time

def menu():
	print("""

db   d8b   db d88888b d8888b.      .d8888.  .o88b. d8888b.  .d8b.  d8888b. d88888b d8888b. 
88   I8I   88 88'     88  `8D      88'  YP d8P  Y8 88  `8D d8' `8b 88  `8D 88'     88  `8D 
88   I8I   88 88ooooo 88oooY'      `8bo.   8P      88oobY' 88ooo88 88oodD' 88ooooo 88oobY' 
Y8   I8I   88 88~~~~~ 88~~~b.        `Y8b. 8b      88`8b   88~~~88 88~~~   88~~~~~ 88`8b   
`8b d8'8b d8' 88.     88   8D      db   8D Y8b  d8 88 `88. 88   88 88      88.     88 `88. 
 `8b8' `8d8'  Y88888P Y8888P'      `8888Y'  `Y88P' 88   YD YP   YP 88      Y88888P 88   YD 
                                                                                           
By: Raz
""")

menu()


# Defining scrape path and request
url_to_scrape = "https://planetdesert.com/collections/cactus"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()

request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')
cacshit = html_soup.find_all('div', class_="grid-product__content")
os.system('clear')
menu()
print("Scraping..")
time.sleep(2)

os.system('clear')
menu()
print("Scraping...")
time.sleep(2)

os.system('clear')
menu()
print("Scraping....")
time.sleep(2)

os.system('clear')
menu()
print("Scraping.")
time.sleep(1)

os.system('clear')
menu()
print("Printing out Contents to a .csv\n[32/100]")
time.sleep(1)

os.system('clear')
menu()
print("Printing out Contents to a .csv\n[53/100]")
time.sleep(1)

os.system('clear')
menu()
print("Printing out Contents to a .csv\n[68/100]")
time.sleep(1)

os.system('clear')
menu()
print("Printing out Contents to a .csv\n[89/100]")
time.sleep(1)

os.system('clear')
menu()
print("Printing out Contents to a .csv\n[100/100]")
time.sleep(1)

os.system('clear')
menu()
print("Done!")


filename = 'products.csv'
f = open(filename , 'w')

headers = 'Title, Price \n'
f.write(headers)

for cactus in cacshit:
	title = cactus.find('div', class_="grid-product__title").text
	price = cactus.find('div', class_="grid-product__price").text
	
	f.write(title + "," + price)

f.close()