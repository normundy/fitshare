from django import forms
from django.contrib.auth.forms import UserCreationForm

class FS_UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(FS_UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
