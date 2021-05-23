from django.urls import path, include

urlpatterns = [
    path('accounts/', include('hospital.authentication.api.v1.urls')),
    path('core/', include('hospital.core.api.v1.urls')),
    path('common/', include('hospital.commons.api.v1.urls')),
    path('user/', include('hospital.user.api.v1.urls')),

]