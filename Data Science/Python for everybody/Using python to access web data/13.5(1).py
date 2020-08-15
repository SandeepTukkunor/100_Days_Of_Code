import json

data = """
{
    "name" : "sandeep",
    "phone":{
        "type" : "intl",
        "number" : "9448028838"

    },
    "email" : {
        "hide" : "yes"
    }

}"""

info = json.loads(data)
print("Name", info["name"])