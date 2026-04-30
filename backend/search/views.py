from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer



class SearchListView(generics.ListAPIView):
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
    