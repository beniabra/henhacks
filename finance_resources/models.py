from django.db import models

# Create your models here.
class Resource(models.Model):
    title = models.CharField(max_length=100)
    COUNTY_CHOICES = [
        ("DE", "Delaware"),
        ("K", "Kent"),
        ("S", "Sussex"),
        ("NC", "New Castle")
    ]
    county = models.CharField(max_length=2, choices=COUNTY_CHOICES)
    categories = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=15, blank=True)
    contact_urls = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1300)

    def __str__(self):
        return self.title