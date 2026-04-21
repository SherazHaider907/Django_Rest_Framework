import requests


# endpoint = "https://httpbin.org/anything"

endpoint = " http://localhost:8000/"

response = requests.get(endpoint)

print(response.text)
print(response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# javaScript Object Notation (JSON) -> Python Dictionary
# print(response.json())