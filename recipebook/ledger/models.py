from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', args=[str(self.name)])

    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.name)])

    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return '{} {}'.format(self.quantity, self.ingredient.name)

    class Meta:
        ordering = ['ingredient']
        verbose_name = 'recipe ingredient'
        verbose_name_plural = 'recipe ingredients'
