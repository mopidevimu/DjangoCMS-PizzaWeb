from django.db import models
from cms.models.pluginmodel import CMSPlugin
# Create your models here.


class Daily_specials(CMSPlugin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="daily_specials")
    description = models.TextField()
    url = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Daily Special"
        verbose_name_plural = "Daily Specials"

    def __unicode__(self):
        return "%s" % (self.name, )


class Menu_Item(CMSPlugin):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_items")
    price = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return "%s" % (self.name, )