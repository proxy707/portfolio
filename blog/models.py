from django.db import models

class Blog(models.Model):
    image=models.ImageField(upload_to="imageofmodel/")
    summary=models.CharField(max_length=200)

