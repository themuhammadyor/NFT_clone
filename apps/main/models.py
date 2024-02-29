from django.db import models

from apps.shared.models import AbstractModel
from apps.users.models import User


# Create your models here.
class Category(AbstractModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(AbstractModel):
    name = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=1000000000, decimal_places=2)
    cover = models.ImageField(upload_to="products/cover/%Y/%m/%d", default="media/product_default.jpg")
    end_in = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_products')
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'products'
