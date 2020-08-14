import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Sadeep</name>
    <phone type = "int">9448028838</phone>
    <email hide = "yes"/>


</person>
'''
tree = ET.fromstring(data)
print("name",tree.find("name").text)
print("Phone:" , tree.find("phone").text)
print("Email", tree.find("email").get("hide"))




