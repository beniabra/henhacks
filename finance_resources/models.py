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
    
class Post(models.Model):
    name=models.CharField(max_length=100,default="anonymous")
    description=models.CharField(max_length=1000)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    likes=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name + " (" + str(self.date_created) + ")"