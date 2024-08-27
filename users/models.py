from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон', blank=True, null=True, help_text='Введите телефонный номер')
    country = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True, help_text='Загрузите аватар')

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


# Create your models here.
