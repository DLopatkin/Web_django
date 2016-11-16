from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Comment(models.Model):
    text = models.TextField()
    work = models.ForeignKey('gallery.Gallery', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    ordering = ('-created_at',)


class Gallery(models.Model):
    IS_AVAILABLE = (
        ("OK", "Available"),
        ("DEL","Deleted"),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    work = models.ImageField(upload_to='member_illust/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=IS_AVAILABLE, default="OK")
    comments = GenericRelation('gallery.Comment', related_query_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)

    def get_comments(self):
        return self.comments
