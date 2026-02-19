from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


# Register your models here.
class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmins(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine,]
    model = Recipe
    search_fields = ('name', )
    list_display = ('name',)
    list_filter = ('name', )


admin.site.register(Recipe, RecipeAdmins)
