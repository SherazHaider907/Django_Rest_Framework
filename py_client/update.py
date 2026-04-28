import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "This is sheraz",
    "price": 100.00
}
response = requests.put(endpoint,json=data)

print(response.json())  