import json

data = """{
    "name" : "sandeep",
    "phone" : {
        "type" : "intl",
        "number" : "948028838"

    },
    "email" :{
        "hide": "yes"
    }
} """

info = json.loads(data)
print("Name", info["name"])




input1 = """[
    {
        "id":"001",
        "x" : "1",
        "name" : "Sandeep"


    },
    {
        "id":"002",
        "x" : "2",
        "name" : "Sunil"

    }
]"""



info2 = json.loads(input1)
for item in info2:
    print("Name", item["name"])
    print("ID", item["id"])
    print("Attribute", item["x"])
        
    