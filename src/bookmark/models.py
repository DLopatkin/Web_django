from django.conf import settings
from django.db import models


class Bookmark(models.Model):
    work = models.ForeignKey('gallery.Gallery')
    comment = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_bookmark')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.work.name
