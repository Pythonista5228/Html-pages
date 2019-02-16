from django.conf.urls import url
from homepage import views

app_name = 'homepage'

urlpatterns = [
    url(r'^time/$', views.time, name='_time'),
    url(r'^$', views.index, name='_index'),
]