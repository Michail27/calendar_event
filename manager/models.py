
from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):
    country = models.TextField()

    def __str__(self):
        return self.country


class ProfileUser(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='user_country')

    class Meta(object):
        unique_together = ('email',)


class ReminderTime(models.Model):
    reminder = models.CharField(max_length=200)

    def __str__(self):
        return self.reminder


class CreateEvent(models.Model):
    user_event = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name="user",
                                   verbose_name="кто создал событие")
    title = models.CharField(max_length=100, verbose_name="название события")
    date_start = models.DateTimeField(verbose_name="Время начало события")
    date_finish = models.DateTimeField(blank=True, null=True, verbose_name="Время окончание события")
    reminder = models.ForeignKey(ReminderTime, verbose_name="Когда напомнить", on_delete=models.CASCADE,
                                 null=True, blank=True, related_name='reminder_user')

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.date_stop is None:
            self.date_finish = self.date_start.replace(hour=23, minute=59, second=59)
        super().save(**kwargs)


class Holidays(models.Model):
    title = models.CharField(max_length=200, verbose_name="Праздник")
    holiday_start = models.DateTimeField(verbose_name="Начала праздника")
    holiday_finish = models.DateTimeField(verbose_name="Окончание праздника")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title






