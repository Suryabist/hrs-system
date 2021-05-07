"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('hospital.api.v1.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='Hospital Referal API', urlconf='hospital.api.v1.urls', url="/api/v1/")
    urlpatterns += [path('api/root/', schema_view),
                    path('', RedirectView.as_view(url='/api/root/', permanent=False)),
                    re_path(r'^__debug__/', include(debug_toolbar.urls)),
                    ]