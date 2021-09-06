from django.db import models


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
