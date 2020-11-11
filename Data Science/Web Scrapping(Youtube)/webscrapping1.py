from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
#opening url and grabbing page
uClint = Ureq(my_url)
page_html = uClint.read()
uClint.close()


#html parser
page_soup = soup(page_html, "html.parser")
#print(page_soup.h1) # prints H1
#print(page_soup.p)# prints paragraphs

#print(page_soup.body.div)

#grab each product 

container = page_soup.findAll("div", {"class": "item-container"})
print(len(container))

print(container[0])