from django.db import models
from account.models import User
from ckeditor.fields import RichTextField


class Chat(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = RichTextField()

    def __str__(self):
        return str(self.user) + " " + self.text[:10]
