from django.urls import path
from .views import RecipeAddView, RecipeListView, RecipeDetailView, RecipeImageAddView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/add', RecipeAddView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image',
         RecipeImageAddView.as_view(),
         name='recipe-add-image')
]

app_name = "ledger"
