from django.urls import include, path
from django.contrib import admin

from heimdalerp import api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
