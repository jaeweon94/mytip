from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):

    sex = forms.CharField(label='성별')
    year = forms.CharField(label='나이')
    job = forms.CharField(label='직업')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )

    def save(self):
        user = super().save()

        profile = Profile.objects.create(
            user = user,
            sex = self.cleaned_data['sex'],
            year = self.cleaned_data['year'],
            job = self.cleaned_data['job'],
        )

        return user