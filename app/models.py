from django.db import models
from django.contrib.postgres.fields import HStoreField
# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="images/product",default="")

    def __str__(self):
        return self.product_name
class user_detail(models.Model):
    user_email=models.CharField(max_length=50)
    user_address1=models.CharField(max_length=50)
    user_address2=models.CharField(max_length=50)
    user_city=models.CharField(max_length=50)
    user_state=models.CharField(max_length=50)
    user_zip=models.IntegerField()
    order=models.JSONField(default=dict)
    def __str__(self):
        return self.user_email
