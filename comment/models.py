from django.db import models
from user.models import User
from newsfeed.models import Newsfeed
from django.utils.timezone import now


class Comment(models.Model):
    post = models.ForeignKey(Newsfeed, related_name='posts', on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)
    time_posted = models.DateTimeField(default=now)

    def __str__(self):
        return f"comment by {id}"

