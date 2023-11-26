from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import *


class HomeViews(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['products'] = Product.objects.all()
        return context


class TeamProductsListViews(ListView):
    model = Product
    template_name = "team_products.html"
    context_object_name = 'products'

    def get_queryset(self):
        team_id = self.kwargs['pk']
        return Product.objects.filter(team_id=team_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs['pk']
        context['team'] = Team.objects.get(id=team_id)
        if context:
            return context



