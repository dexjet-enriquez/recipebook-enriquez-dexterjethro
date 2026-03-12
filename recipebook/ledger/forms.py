from django import forms
from .models import Recipe, RecipeImage


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author',]


class RecipeImageAddForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description',]
