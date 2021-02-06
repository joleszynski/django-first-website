from django.db import models
from colorfield.fields import ColorField


class Trainer(models.Model):
    photo = models.ImageField(default="", upload_to="team/trainers/")
    name = models.CharField(max_length=100)
    dance_type = models.CharField(max_length=200)
    describe = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    photo = models.ImageField(default="", upload_to="team/groups/")
    name = models.CharField(max_length=100)
    dance_type = models.CharField(max_length=100)
    describe = models.TextField(max_length=255)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class TeamDescribe(models.Model):
    photo = models.ImageField(default="", upload_to="team/describe/")
    describe = models.TextField(max_length=355)
    is_active = models.BooleanField(default=False)

    #def __str__(self):
    #    return self.name
