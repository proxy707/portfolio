from django.db import models

class Blog(models.Model):
    tiltle=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to="imageofmodel/")


 