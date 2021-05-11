from rest_framework import routers

from hospital.core.api.v1.views.hospital import hospitalViewSet, IcuBedViewSet, NormalBedViewSet, VentilatorsBedViewSet

router = routers.DefaultRouter()
router.register('hospital', hospitalViewSet)
router.register('icubeds', IcuBedViewSet)
router.register('normalbeds', NormalBedViewSet)
router.register('ventailators', VentilatorsBedViewSet)

urlpatterns = router.urls
