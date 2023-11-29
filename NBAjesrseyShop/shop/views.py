from django.shortcuts import render
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


class ProductDetailVeiw(View):
    model = Product
    template_name = 'detail_product.html'
    context_object_name = 'detail'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Product.objects.filter(id=product_id)

    def get(self, request, pk):
        product_variant = ProductVariant.objects.all()
        size = [s for s in product_variant]

        product = Product.objects.get(pk=pk)
        description = product.description
        player= product.nba_player
        image = product.image
        team = product.team_id
        
        context = {
                'size': size,
                'description': description,
                'player': player,
                'image': image,
                'team': team,
        }
        return render(request, 'detail_product.html', context)

