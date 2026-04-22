from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):

    """
    DRF API View

    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sale_price'])
    return Response(data)

































# import json
# from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse

# from products.models import Product
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price'])
#     #     json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str, header={"Content-Type": "application/json"})
#     return JsonResponse(data)


# import json
# from django.http import JsonResponse
# from products.models import Product
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price
#     return JsonResponse(data)


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