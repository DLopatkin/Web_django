from django.db import models
from django.contrib.auth.models import AbstractUser


class Myuser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main_page:user', kwargs={'pk': self.id})
