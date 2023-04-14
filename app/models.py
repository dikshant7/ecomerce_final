from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.utils.timezone import now
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
    feature1=models.CharField(max_length=50,default="")
    feature2=models.CharField(max_length=50,default="")
    feature3=models.CharField(max_length=50,default="")
    feature4=models.CharField(max_length=50,default="")
    actual_price=models.IntegerField(default=0)
    

    def __str__(self):
        return self.product_name
class user_detail(models.Model):
    user_email=models.CharField(max_length=50)
    user_address1=models.CharField(max_length=50,default="")
    user_city=models.CharField(max_length=50,default="")
    user_state=models.CharField(max_length=50,default="")
    user_zip=models.IntegerField(default=0)
    order=models.JSONField(default=dict)
    order_history=models.JSONField(default=dict)
    order_buynow=models.IntegerField(default=1)
    quant_buynow=models.IntegerField(default=1)
    def __str__(self):
        return self.user_email
class order(models.Model):
    product_id=models.IntegerField()
    created_date = models.DateTimeField(default=now, editable=False)
    quant=models.IntegerField()
    user_email=models.CharField(max_length=50,default="")

            
