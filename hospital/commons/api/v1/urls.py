from rest_framework import routers

from hospital.commons.api.v1.views.contact import ContactViewSet
from hospital.commons.api.v1.views.corona import coronaViewSet

router = routers.DefaultRouter()
router.register('corona', coronaViewSet)
router.register('contact', ContactViewSet)
urlpatterns = router.urls
