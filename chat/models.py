from django.db import models
from account.models import User


class Chat(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return str(self.user) + " " + self.text[:10]
