from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    messages = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=250)
    body= models.TextField()
    pub_date= models.DateTimeField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
