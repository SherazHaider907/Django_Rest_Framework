import requests

product_id = input("Enter the product id to delete: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'Invalid product id: {product_id}')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

response = requests.delete(endpoint)

print(response.status_code, response.status_code == 204)  