from django.urls import path

from . import views

urlpatterns = [
    path('',views.product_list_create_view , name='product-list'),
    path('<int:pk>/',views.Product_detail_View, name='product-detail'),
]
