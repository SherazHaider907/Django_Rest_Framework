import requests


# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint,params={"abc":123},json={"query":"hello world"})
# print(response.headers)
# print(response.text)
# print(response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# javaScript Object Notation (JSON) -> Python Dictionary

print(response.json())