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