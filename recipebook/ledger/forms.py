from django import forms
from .models import Recipe


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author',]
