from django.urls import path

from . import views

urlpatterns = [
    # class base view
    path('',views.product_list_create_view),
    path('<int:pk>/update/',views.Product_update_View ),
    path('<int:pk>/delete/',views.Product_delete_View),
    path('<int:pk>/',views.Product_detail_View),

    # # function based view
    # path('',views.product_alt_view , name='product-list'),
    # path('<int:pk>/',views.product_alt_view, name='product-detail'),
]
