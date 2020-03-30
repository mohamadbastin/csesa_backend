from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Participant(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram_user = models.OneToOneField('TelegramUser', on_delete=models.CASCADE)
    # name = models.CharField(max_length=256)
    # phone = models.CharField(max_length=15)
    # telegram_username = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return str(self.telegram_user)


class TelegramUser(models.Model):
    name = models.CharField(max_length=512)
    username = models.CharField(max_length=512,)
    telegram_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
