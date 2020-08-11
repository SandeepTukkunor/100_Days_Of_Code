#scrapping the web 
#insatll beautiful soupe 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")


#retrive all the anchor tags 
tags = soup("a")

for tag in tags:
    print(tag.get("href", None))


# pip install --upgrade html5lib==1.0b8, This has solved the error