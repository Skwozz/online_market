from rest_framework.routers import DefaultRouter

from api.views import PurchaseModelViewSet,UserModelViewSet, WarehouseModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('warehouse', WarehouseModelViewSet)
router.register('product', ProductModelViewSet)
router.register('purchase', PurchaseModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)