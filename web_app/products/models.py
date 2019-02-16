from django.db import models

# Create your models here.

class Category(models.Model):
   category_name = models.CharField(max_length=40)
   category_slug = models.SlugField(unique=True)
   
   def __str__(self):
       return self.category_name


class products(models.Model):
    Category_title = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    product_price = models.IntegerField(default=100)
    product_description = models.CharField(max_length=500)
    product_rating = models.IntegerField(default=5)
    product_quantity = models.IntegerField(default=10)

    def __str__(self):
        return self.product_name

