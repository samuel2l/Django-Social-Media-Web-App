from django import forms


class ChatForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=1000)