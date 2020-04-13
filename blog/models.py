from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" %(self.title, )


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    content = models.TextField()

    def __unicode__(self):
        return "%s" % (self.title, )