import requests
import json

# set url that we want to get data from
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

# pass the url variable to get method that is part of the requests module and assign it variable "response"
response = requests.get(url)

# 'requests.get' returns a response object, therefore join it with '.text' to get the json data 
# pass the response_body to the json parser; takes the JSON formatted data and turn it into a list
data = json.loads(response.text)
# for proper readability
print(json.dumps(data, indent=4, sort_keys=True))

