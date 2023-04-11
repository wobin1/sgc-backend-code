from django.db import models
from user.models import User
from django.utils.timezone import now


class Newsfeed(models.Model):
    posted_by = models.ForeignKey(User, related_name='newsfeed', on_delete=models.CASCADE)
    feed = models.CharField(max_length=300)
    imageLink = models.CharField(max_length=600)
    likes = models.IntegerField(default=0)
    time_posted = models.DateTimeField(default=now)

    def __str__(self):
        return f"By {self.posted_by}"