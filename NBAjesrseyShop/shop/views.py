from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import *


class TeamListViews(ListView):
    model = Team
    template_name = "home.html"
    context_object_name = 'team'


class ProductListViews(ListView):
    model = Product
    template_name = "shop_team.html"
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        team_id = self.kwargs['pk']
        return Product.objects.filter(team_id=team_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs['pk']
        context['team'] = Team.objects.get(pk=team_id)
        return context




