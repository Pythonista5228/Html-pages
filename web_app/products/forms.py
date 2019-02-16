from django import forms
from . import models

class AddProduct(forms.ModelForm):
  class Meta:
    model = models.products
    fields = ['product_name','slug','product_price','product_description','product_rating','product_quantity','Category_title']