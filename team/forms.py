"""
These is a form which will be displayed in
user management section when user is super user
to manage team cards without using admin page
"""
from django import forms
from .models import InstructorProfile


class InstructorProfileForm(forms.ModelForm):
    """ Instructor profile form """
    class Meta:
        model = InstructorProfile
        fields = ('name', 'age', 'about', 'image',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove auto-generated lables,
            set focus on the first field in form """

        super().__init__(*args, **kwargs)
        self.fields['about'].widget.attrs = {'rows': 3}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'image':
                self.fields[field].widget.attrs['placeholder'] = False
            else:
                self.fields[field].widget.attrs['placeholder'] = '...'
            self.fields[field].widget.attrs['class'] = 'add-form-input'
