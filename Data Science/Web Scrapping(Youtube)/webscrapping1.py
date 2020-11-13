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

containers = page_soup.findAll("div", {"class": "item-container"})
print(len(containers))


# to open a file 
file_name = "product.csv"
f = open(file_name, "w")
headers = "Brand", "prouct name", "Shipping\n"

f.write("Brand, product name, shippig\n" )

#below 3 lines of code is for container 1 that is 0th
#container = containers[0]
#print(container.a)
#print(container.div.div.a.img["title"]) # will return the title 



# so for all the containers title, we can write for loop 
for container in containers:
    brand = container.div.div.a.img["title"]
    print("brand: " + brand)
    #for parsing the title
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    print("product_name: " +  product_name )
    # grab shipping price(because some of them are not having price)
    #price_of_product = container.findAll("li", {"class":"price-current-label"})
    #print(price_of_product)

    #shipping price
    shipping_container = container.findAll("li", {"class":"price-ship"})
    
    shipping_container_price = shipping_container[0].text.strip()
    print("shipping_container_price: " + shipping_container_price )
    f.write(brand + "," +  product_name.replace(",", "|") + "," + shipping_container_price + "\n")
    

f.close()


