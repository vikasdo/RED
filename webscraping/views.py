from bs4 import BeautifulSoup
import urllib.request as requested

import requests



from difflib import get_close_matches
import webbrowser



from django.http import HttpResponse
from django.shortcuts import render
class product:
    def __init__(self, name=None, price=None,image=None,cat=None):
        self.name = name
        self.price = price
        self.image=image
        self.cat=cat
def index(request):
    return render(request, "home.html")
def search(request):
    product_array=request.GET['key']
    product_arr = product_array.split()


    key = ''
    for word in product_arr:

        if len(product_arr) == 1:
            key = key + str(word)
        else:
            key = key + '+' + str(word)
    print(key)

    print(key)

    # snapdeal **)))))))_++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    url_flip = 'https://www.snapdeal.com/search?keyword=' + str(key) + ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    keys = []
    source_code = requests.get(url_flip, headers=headers)
    plain_text = source_code.text
    soup_flip = BeautifulSoup(plain_text, "html.parser")
    snapdeal = []
    count = 0
    try:
        for title in soup_flip.find_all("p", {"class": "product-title"}):
            count += 1

            keys.append(title.text)

            if count == 2:
                break
    except:
        print()
    values = []
    try:
        k = 0
        for div in soup_flip.find_all('div', {'class': 'product-price-row clearfix'}):
            for each in div.find_all('span', {'class': 'lfloat product-price'}):
                if k < 2:
                    values.append(each.text.replace("shipping", " "))
                    k += 1
    except:
        print()
    response1 = requested.urlopen(url_flip)
    soup = BeautifulSoup(response1, 'html.parser')
    s = soup.find_all('picture', {'class': 'picture-elem'})
    c = 0
    imag = []
    for s1 in s:
        try:
            if c < 2:
                imag.append(s1.img['data-src'])
                c += 1
        except:
            print()
    for i in range(len(keys)):
        snapdeal.append(product(keys[i], values[i], imag[i], 'Snapdeal'))
    #    flipkart ********************************************************************************
    url = 'https://www.flipkart.com/search?q=' + str(key) + ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    flipkart=[]
    titlear=[]
    prices = []
    c=0
    for title in soup.find_all('div', {'class': '_3wU53n'}):
        if c<2:
         titlear.append(title.text)
         c+=1
    try:

        product_source_code = requests.get(url, headers=headers)
        product_plain_text = product_source_code.text
        product_soup = BeautifulSoup(product_plain_text, "html.parser")
        c = 0

        for price in product_soup.find_all('div', {'class': '_1vC4OE'}):
            if c<2:
             prices.append(price.text)
             c+=1
    except:
        print("erre")
    for i in range(len(titlear)):
        flipkart.append(product(titlear[i],prices[i],cat='Flipkart'))



    #ebay**************************************************************************************************************************


    url_flip = 'https://www.ebay.com/sch/i.html?_nkw=' + str(key) + ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    title_arr = []
    source_code = requests.get(url_flip, headers=headers)
    plain_text = source_code.text
    soup_flip = BeautifulSoup(plain_text, "html.parser")
    count = 0
    tty=[]
    try:

        for title in soup_flip.find_all("h3", {"class": "s-item__title"}):

            count += 1

            tty.append(title.text)
            if count == 2:
                break
    except:
        print()
    pr=[]
    pr2=[]
    try:
        k = 0
        for div in soup_flip.find_all('div', {'class': 's-item__wrapper clearfix'}):
            for each in div.find_all('div', {'class': 's-item__detail s-item__detail--primary'}):
                if k < 2 and each.text not in('or Best Offer','Watch','Buy It Now'):
                    pr.append(each.text)
            k += 1


    except:
        print()
    url = 'https://www.ebay.com/sch/i.html?_nkw='+str(key)+''
    response = requested.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    img=[]
    s = soup.find_all('div', {'class': 's-item__image-wrapper'})
    for s1 in s:
        try:
            img.append(s1.img['src'])
        except:
            print("not found")

    ebay=[]
    for i in range(len(tty)):
     ebay.append(product(tty[i], pr[i],img[i], cat='Ebay'))


    return render(request, "home.html", {'snapdeal': snapdeal,'flipkart':flipkart,'ebay':ebay})

