from django import forms


class Contact(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
