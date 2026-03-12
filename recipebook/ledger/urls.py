from django.urls import path
from .views import RecipeAddView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeAddView.as_view(), name='recipe-add'),
]

app_name = "ledger"
