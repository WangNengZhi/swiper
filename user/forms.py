from django import forms

from user.models import User
from user.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'gender', 'birthday', 'location']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        """检查并清洗max_distance"""
        cleaned_data = super().clean()
        if cleaned_data['max_distance'] >= cleaned_data['min_distance']:
            return cleaned_data['max_distance']
        else:
            raise forms.ValidationError('max_distance不能小于min_distance')

    def clean_max_dating_age(self):
        """检查并清洗max_dating_age"""
        cleaned_data = super().clean()
        if cleaned_data['max_dating_age'] >= cleaned_data['min_dating_age']:
            return cleaned_data['max_dating_age']
        else:
            raise forms.ValidationError('max_dating_age不能小于min_dating_age')
