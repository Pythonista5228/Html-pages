from django.db import models
from products.models import products
# Create your models here.


class User_Address(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

class User_Credential(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=15)
    user_email = models.EmailField(unique=True)
    user_mobile = models.IntegerField(unique=True)
    user_address = models.ForeignKey(User_Address, on_delete=models.CASCADE)
    user_register_date = models.DateTimeField(auto_now_add=True)

class User_Card_Details(models.Model):
    user_id = models.ForeignKey(User_Credential, on_delete=models.CASCADE)
    user_credit_card = models.IntegerField(unique=True)
    user_credit_card_expiry_month = models.IntegerField()
    user_credit_card_expiry_year = models.IntegerField()
    user_debit_card = models.IntegerField(unique=True)
    user_debit_card_expiry_year = models.IntegerField()
    user_debit_card_expiry_year = models.IntegerField()

class User_Login_Logout_details(models.Model):
    user_id = models.ForeignKey(User_Credential, on_delete=models.CASCADE)
    user_login_timestamp = models.DateTimeField(auto_now_add=True)
    user_logout_timestamp = models.DateTimeField(auto_now_add=True)

class User_Wishlist(models.Model):
    user_id = models.ForeignKey(User_Credential, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)