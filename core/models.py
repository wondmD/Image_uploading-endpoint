from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    format = models.CharField(max_length=10)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/')
    blur_data_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.filename
