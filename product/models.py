# django core imports
from django.db import models
from django.utils import timezone

# third-party imports
from ckeditor.fields import RichTextField


class Product(models.Model):

    TAGS = [
        ("computer", "Computer"),
        ("airpod", "Air Pod"),
        ("iwatch", "iWatch"),
    ]

    thumbnail = models.ImageField(upload_to="thumbnail/")
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = RichTextField(null=True, blank=True)
    tags = models.CharField(max_length=200, choices=TAGS)
    created_at = models.DateField(default=timezone.now)

    # class Meta:
    #     # ordering = ["created_at"]

    def __str__(self):
        return self.name