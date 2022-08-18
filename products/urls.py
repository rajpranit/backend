from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/' , views.product_mixin_view, name="productdetail"),
    path('<int:pk>/update' , views.product_mixin_view, name="productupdate"),
    path('<int:pk>/delete' , views.product_mixin_view, name="productdelete"),

    path('', views.product_mixin_view, name=('productcreate')),

]