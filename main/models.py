from django.db import models


class SketchImage(models.Model):
    image = models.ImageField(upload_to='uploads/')

