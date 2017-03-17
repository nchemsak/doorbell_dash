from django.contrib.auth.models import User
from django.db import models

class Photo(models.Model):
    # post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="")

    class Meta:
        verbose_name_plural = 'Photos'
