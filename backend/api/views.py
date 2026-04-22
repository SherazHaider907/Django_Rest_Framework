import json
from django.http import JsonResponse
from products.models import Product
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
































































# def api_home(request, *args, **kwargs):

#     # request -> HttpRequest -> Django's way of representing HTTP Requests as Python objects
#     # request.body -> byte string of data
#     print(request.GET) # url query params -> request.GET
#     print(request.POST) # form data -> request.POST
#     body = request.body # byte string of data -> string of data -> python dict  
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     # return JsonResponse({"message": "Hello This is your django api response!!", "status": "success"})
#     return JsonResponse(data)