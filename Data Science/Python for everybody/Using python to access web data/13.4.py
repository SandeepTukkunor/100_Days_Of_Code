
import xml.etree.ElementTree as ET
from urllib.request import urlopen

with urlopen("http://py4e-data.dr-chuck.net/comments_868728.xml") as url:
    xml = url.read()


total_number = 0
tot_sum = 0


print("retriving", url)



print("retrived:", len(xml), "charecters")



tree =  ET.fromstring(xml)
counts = tree.findall(".//count")
for item in counts:
    tot_sum = tot_sum + int(item.text)
    total_number = total_number + 1

print("count: ", total_number)
print("Sum: ", tot_sum)

