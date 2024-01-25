from django import forms

from moneytrack_app.models import Category


class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
