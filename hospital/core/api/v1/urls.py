from rest_framework import routers

from hospital.core.api.v1.views.hospital import hospitalViewSet

router = routers.DefaultRouter()
router.register('hospital', hospitalViewSet)

urlpatterns = router.urls
