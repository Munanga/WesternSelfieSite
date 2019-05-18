from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill,ResizeToFit,SmartResize,Transpose,ResizeToCover,Thumbnail,SmartCrop

# Create your models here.

class ImageModel(models.Model):
    caption = models.CharField(max_length=32)
    #image = models.ImageField(upload_to='media/')

    image = ProcessedImageField(upload_to='media',
                                 processors=[Transpose(),SmartResize(550,550)],
                                 format='JPEG',
                                 options={'quality':90},null=True
                                )

    upload_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.caption


