import requests


endpoint = "http://localhost:8000/api/products/10980/"

response = requests.get(endpoint)

print(response.json())  