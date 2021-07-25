from django import forms


class Students(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)
