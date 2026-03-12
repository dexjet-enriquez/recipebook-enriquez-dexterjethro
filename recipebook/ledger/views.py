from django.http import HttpResponse
from django.shortcuts import render
from django.tasks import Task
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, RecipeImage
from .forms import RecipeAddForm, RecipeImageAddForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_add_form.html'
    form_class = RecipeAddForm
    success_url = reverse_lazy('ledger:recipe-list')

    def get_context_data(self, **kwargs):  # done to fix form conflict login form
        context = super().get_context_data(**kwargs)
        context['recipe_add_form'] = context.get('form')
        context['form'] = None
        return context


class RecipeImageAddView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'ledger/recipe_add_image_form.html'
    form_class = RecipeImageAddForm
    success_url = reverse_lazy('ledger:recipe-detail')

    def get_context_data(self, **kwargs):  # done to fix form conflict login form
        context = super().get_context_data(**kwargs)
        context['recipe_add_image_form'] = context.get('form')
        context['form'] = None
        return context

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.kwargs['pk']})
