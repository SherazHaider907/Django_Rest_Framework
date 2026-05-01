from rest_framework import generics
from products.models import Product
from rest_framework.response import Response

from products.serializers import ProductSerializer

from . import client
class SearchListView(generics.GenericAPIView):
    def get(self,request,*args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0" 
        tag = request.GET.get('tag') or None
        if not query:
            return Response('',status=400)
        results = client.perform_search(query, tag=tag,user= user,public = public)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        result = Product.objects.none()
        if query is not None:
            user  = None
            if self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(query,user= user)
        return result
    