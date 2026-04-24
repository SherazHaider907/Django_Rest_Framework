from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = "pk"??

Product_detail_View = ProductDetailAPIView.as_view()