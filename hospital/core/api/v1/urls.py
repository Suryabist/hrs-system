from rest_framework import routers

# from hospital.core.api.v1.views.hospital import hospitalViewSet, IcuBedViewSet, NormalBedViewSet, VentilatorsBedViewSet, \
#     OxygenBedViewSet, DeathViewSet, DischargeViewSet
from hospital.core.api.v1.views.hospital import hospitalViewSet, IcuBedViewSet, NormalBedViewSet, VentilatorsBedViewSet, \
    OxygenBedViewSet, DeathViewSet, DischargeViewSet, HduBedsViewSet

router = routers.DefaultRouter()
router.register('hospital', hospitalViewSet)
router.register('icubeds', IcuBedViewSet)
router.register('normalbeds', NormalBedViewSet)
router.register('ventailators', VentilatorsBedViewSet)
router.register('hdubeds', HduBedsViewSet)
router.register('oxygen', OxygenBedViewSet)
router.register('death', DeathViewSet)
router.register('discharge', DischargeViewSet)
router.register('focalperson', DischargeViewSet)

urlpatterns = router.urls
