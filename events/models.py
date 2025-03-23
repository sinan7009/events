from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue name',max_length=124)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('zip code',max_length=15)
    phone = models.CharField('phone number', max_length=15)
    web = models.URLField('web address')
    email_address = models.EmailField('Email address')

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('user email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Events(models.Model):
    name = models.CharField('Events name',max_length=124)
    event_date = models.DateTimeField('Events date')
    venue = models.ForeignKey(Venue, blank=True , null= True, on_delete=models.CASCADE)
    manager = models.CharField(max_length= 124)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyclubUser, blank=True)

    def __str__(self):
        return self.name