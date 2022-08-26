from rest_framework import routers
from products.viewsets import ProductView

router = routers.SimpleRouter()
router.register('product', ProductView, basename='product')
print(router.urls)
urlpatterns = router.urls