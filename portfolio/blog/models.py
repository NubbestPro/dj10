from django.db import models

#add blog app into setting, url, views, html

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.body

#title CharField
#pub_date DateTimeField
#body TextField
#image ImageField

#python manage.py makemigrations
#python manage.py migrate
#add to admin
#def __str

#update views
#update blog.html