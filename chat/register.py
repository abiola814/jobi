from django import forms

class RegisterUser(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, firstname, lastname, username, email, password, confirm_password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['c-password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['c-password']