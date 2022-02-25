from .models import Chat
from django import forms
from ckeditor.widgets import CKEditorWidget


class ChatForm(forms.ModelForm):

    text = forms.CharField(widget=CKEditorWidget() , label="Message:") 


    class Meta:
        model = Chat
        fields = ["text"]


    def save(self , commit=True , user=None):
        obj = Chat(text = self.cleaned_data['text'] , user = user)
        if commit:
            return obj.save()
        else:
            return obj
    