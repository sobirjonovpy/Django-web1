from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')
    url = models.URLField()


    def __str__(self):
        return self.title     
    













