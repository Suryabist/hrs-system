from django.urls import path, include

urlpatterns = [
    path('core/', include('hospital.core.api.v1.urls')),
    path('common/', include('hospital.commons.api.v1.urls'))
]