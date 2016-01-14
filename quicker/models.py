from django.db import models

# Create your models here.

class ItemBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Car(ItemBase):
    model_description = models.CharField(max_length=500)
    company = models.ForeignKey('Car_Company')
    url = models.CharField(max_length=500)
    price = models.IntegerField()
    location = models.CharField(max_length=300,default='Delhi')

    def __unicode__(self):
        return self.model_description

class Car_Company(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name