from .models import Chat
from django import forms


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ["text"]


    def save(self , commit=True , user=None):
        obj = Chat(text = self.cleaned_data['text'] , user = user)
        if commit:
            return obj.save()
        else:
            return obj
    