from django.db import models
from user.models import User


class Suggestion(models.Model):
    posted_by = models.ForeignKey(User, related_name="suggestions", on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=300)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'suggestion by {self.posted_by}'


