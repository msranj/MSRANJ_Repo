## make sure to install all the necessary libraries
## reference
## https://github.com/KashmalaJamshaid/Web-scraping-using-python-and-beautifulsoup/blob/main/Web_Scraping_using_python_and_beautifulsoup.ipynb
## Beautiful Soup 4 Tutorial #1 - Web Scraping With Python https://www.youtube.com/watch?v=gRLHr664tXA



from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur

# reading a .html file
with open(r"C:\Users\prade\Downloads\BeautifulSoup Tutorial How to Parse Web Data With Python.html",'r', encoding='utf-8') as f:
        doc = BeautifulSoup(f,"html.parser")

    # print(doc.prettify())

# finding the .html file with tag

tag = doc.title()
tag.string = "hello"
print(tag)
print(tag.string)





 