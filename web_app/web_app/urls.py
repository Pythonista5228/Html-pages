from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^homepage/',include('homepage.urls')),
    url(r'^products/',include('products.urls')),
    url(r'admin/', admin.site.urls),
]