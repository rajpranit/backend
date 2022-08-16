from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/' , views.product_detail_view, name="productdetail"),
    path('<int:pk>/update' , views.product_update_view, name="productupdate"),
    path('', views.product_list_create_view, name=('productcreate')),

]