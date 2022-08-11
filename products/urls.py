from django.urls import path
from .views import ProductDetailView , ProductCreateView

urlpatterns = [
    path('<int:pk>/' , ProductDetailView.as_view(), name="producedetail"),
    path('', ProductCreateView.as_view(), name=('productcreate'))

]