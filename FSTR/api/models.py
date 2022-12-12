from django.db import models
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator], primary_key=True)
    phone = PhoneNumberField(null=True, blank=True)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)


class Coords(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    height = models.IntegerField()


class Level(models.Model):
    winter = models.CharField(max_length=10, blank=True)
    summer = models.CharField(max_length=10, blank=True)
    autumn = models.CharField(max_length=10, blank=True)
    spring = models.CharField(max_length=10, blank=True)


class PerevalAdded(models.Model):
    STATUS_CHOISES = (('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected'))
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=15)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=50)
    connect = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    add_time = models.DateTimeField(blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOISES, default='new')


class PerevalImages(models.Model):
    title = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    data = models.BinaryField()
    pereval_added = models.ForeignKey(PerevalAdded, related_name='images', on_delete=models.CASCADE)
