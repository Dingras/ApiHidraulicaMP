from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    url_img = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
