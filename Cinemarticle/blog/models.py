from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField
    blog_name = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    content = models.CharField(max_length=5000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='blog/images', default="")
    trailer = models.CharField(max_length=250)

    def __str__(self):
        return self.blog_name