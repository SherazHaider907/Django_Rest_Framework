from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.Product_detail_View, name='product-detail'),
]
