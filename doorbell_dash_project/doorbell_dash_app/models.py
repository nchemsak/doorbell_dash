from django.contrib.auth.models import User
from django.db import models
from django.core.files import File  # you need this somewhere
import urllib

class Photo(models.Model):
    # url = models.CharField(max_length=255, unique=True)
    # post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField('img', upload_to='photos/', default='photos/None/No-img.jpg')
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Photos'

    # def __str__(self):
    #     return str(self.image)

# def photo_post(request):
#     request.POST

photo = Photo()
photo.image = "photos/image.jpg"
photo.save()


class CachedImage(models.Model):
    url = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='photos/', blank=True)

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0]))
                    )
            self.save()


