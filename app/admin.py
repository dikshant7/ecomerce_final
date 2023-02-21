from django.contrib import admin

# Register your models here.
from .models import product
admin.site.register(product)

from .models import user_detail
admin.site.register(user_detail)