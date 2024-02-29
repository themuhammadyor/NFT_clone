from django.contrib import admin

from apps.main.models import Category, Product

# Register your models here.
admin.site.register([Category, Product])
