## make sure to install all the necessary libraries
## reference
    ## https://github.com/KashmalaJamshaid/Web-scraping-using-python-and-beautifulsoup/blob/main/Web_Scraping_using_python_and_beautifulsoup.ipynb
    ## Beautiful Soup 4 Tutorial #1 - Web Scraping With Python https://www.youtube.com/watch?v=gRLHr664tXA
    ## https://tedboy.github.io/bs4_doc/generated/generated/bs4.BeautifulSoup.html#methods


# ------------------------- how to read from .html file stored in local disk --------------------------------
from bs4 import BeautifulSoup
# import urllib
# from urllib import request
# import urllib.request as ur

# reading a .html file
# with open(r"C:\Users\prade\Downloads\BeautifulSoup Tutorial How to Parse Web Data With Python.html",'r', encoding='utf-8') as f:
# doc = BeautifulSoup(f,"html.parser")

# print(doc.prettify())

# finding the .html file with tag

# tag = doc.title()
# tag.string = "hello world"
# print(tag)
# print(tag.string)


# find the tags that are first to occur in the document
# tag = doc.find("quote")
# tag = doc.find_all("p")[0]

# print(tag[0])
 
# ------------------------- how to read from website --------------------------------
    # install requests library by using
    # pip install requests

import requests

url = "https://www.mightyape.co.nz/mn/canon/shop/category/electronics/cameras-video/lenses/"

result = requests.get(url)

print(result.text) 





