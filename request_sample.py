import requests


# MAKE AN OBJECT TO STORE THE DATA OF THE REQUEST
URL = 'https://alternateco.com/blog/api/v1/posts/2/'
r = requests.get(URL)

# USE METHOD obj.json() TO GET AS json
print(r.json())

# SHOW THE STATUS CODE OF A REQUEST WHICH IF IS SUCCESSFUL 200 WOULD BE THE STATUS CODE
print(r.status_code)


# FILTERING ThE JSON BY IT'S KEYS
# FIRST MAKE A VARIABLE THAT STORES THE JSON
json_filter = r.json()

# FOLLOW THE SYNTAX
# IN THE BRACKET YOU MUST CHOOSE A KEY NOT SPECIFICALLY ONLY ONE KEY ALTHOUGH YOU CAN MULTIPLE KEYS

# print (json_filter[key_1][key2])
print(json_filter["title"])
