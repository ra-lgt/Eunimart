from django import forms


class user_cred(forms.Form):
    first_name=forms.CharField(max_length=50)
    middle_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    phone_number=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=10000,widget=forms.PasswordInput)