from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['title', 'content', 'file_upload', 'phone_number', 'kakao_id', 'bank', 'account_number', 'real_name', 'agree']
        # labes와 fields... fields는 [], labels는 {}
        labels = {
            'title': '제목',
            'content': '소개글',
        }