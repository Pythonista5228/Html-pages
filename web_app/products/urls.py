from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^addproduct/$', views.product_create, name="addproduct"),
    url(r'^products/$', views.list_of_products, name="list_of_product"),
]