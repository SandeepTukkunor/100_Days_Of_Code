#scrapping the web 
#insatll beautiful soupe 
"""
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
"""


# pip install --upgrade html5lib==1.0b8, This has solved the error




"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')
numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))
"""




import urllib.request as ur
from bs4 import *

current_repeat_count = 0
url = "http://py4e-data.dr-chuck.net/known_by_Kylian.html"
repeat_count = int(input('Enter count: '))
position = int(input('Enter position: '))


def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)