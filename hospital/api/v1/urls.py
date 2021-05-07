from django.urls import path, include

urlpatterns = [
    path('core/', include('hospital.core.api.v1.urls')),

]