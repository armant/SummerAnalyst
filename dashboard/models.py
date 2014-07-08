from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Firm(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    STATUSES = (
        ('C', 'Considering'), ('A', 'Applying'),
        ('1', 'Preparing for the 1-round'), ('2', 'Preparing for the 2-round'),
        ('3', 'Preparing for the 3-round'), ('4', 'Preparing for the 4-round'),
        ('5', 'Preparing for the 5-round'), ('6', 'Preparing for the 6-round'),
        ('7', 'Preparing for the 7-round'), ('8', 'Preparing for the 8-round'),
        ('9', 'Preparing for the 9-round'), ('S', 'Preparing for the Superday')
    )
    app_status = models.CharField(max_length=26, choices=STATUSES, blank=True)
    deadline = models.DateField(blank=True, null=True)
    reminder_date = models.DateField(blank=True, null=True)
    reminder_recurrence_number = models.PositiveSmallIntegerField(blank=True,
            null=True)
    PERIODS = (
        ('D', 'day(s)'), ('W', 'week(s)'), ('M', 'month(s)'), ('Y', 'year(s)')
    )
    reminder_recurrence_type = models.CharField(max_length=8, choices=PERIODS,
            blank=True)


    def __unicode__(self):
        return self.name


class Contact(models.Model):
    firms = models.ManyToManyField(Firm)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True)
    last_contact_date = models.DateField(blank=True, null=True)
    reminder_recurrence_number = models.PositiveSmallIntegerField(blank=True,
            null=True)
    PERIODS = (
        ('D', 'day(s)'), ('W', 'week(s)'), ('M', 'month(s)'), ('Y', 'year(s)')
    )
    reminder_recurrence_type = models.CharField(max_length=8, choices=PERIODS,
            blank=True)
    reminder_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User)
    reminder_days = models.PositiveSmallIntegerField(default=1, blank=True,
            null=True)