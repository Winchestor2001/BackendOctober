from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    stst = (
        ('salom', 'salom'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    complated = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    st = models.CharField(max_length=255, choices=stst)

    def __str__(self):
        return f"{self.user} - {self.title}"
