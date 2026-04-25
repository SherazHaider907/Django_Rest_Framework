import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "hello world",
    "content": "this is some content",
    "price": 123.00
}

response = requests.post(endpoint , json=data)

print(response.json())  