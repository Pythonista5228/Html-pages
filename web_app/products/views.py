from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from products.models import products , Category

# Create your views here.


def product_create(request):
    if request.method == "POST":
      form = forms.AddProduct(request.POST)  
      #reqest.files for the file upload
      #save product to the database
      form.save()
      product = products.objects.all()
      return render(request,'product/products.html',{'product':product})
    else:
      form = forms.AddProduct()
      category = Category.objects.all()
      categories_context = {
        'category_name' : category,
        'form' : form,
        }

    return render(request,'product/addproduct.html',categories_context)

def list_of_products(request):
   product = products.objects.all()
   print(product)
   return render(request,'product/products.html',{'product':product})

def update_products(request):
   form = forms.AddProduct()
   return render(request,'product/addproduct.html',{'from':form})  