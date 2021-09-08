from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """ "Product" chet
    Product title
    Product link
    Product price
    Product created date of record
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """ "Products wishlist" chet

    owner
    products - ManyToMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
