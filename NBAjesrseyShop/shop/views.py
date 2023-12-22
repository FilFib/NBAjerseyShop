from django.shortcuts import render
from .models import *
from django.views.generic import *
from cart.forms import CartAddProductForm


class HomeViews(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['products'] = Product.objects.filter(
            productvariant__stock_quantity__gt=0).distinct()
        return context


class TeamProductsListViews(ListView):
    model = Product
    template_name = "team_products.html"
    context_object_name = 'products'

    def get_queryset(self):
        team_id = self.kwargs['pk']
        return Product.objects.filter(team_id=team_id,
        productvariant__stock_quantity__gt=0).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs['pk']
        context['team'] = Team.objects.get(id=team_id)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail_product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            is_out_of_stock = bool(self.kwargs.get('is_out_of_stock', False))
            product_variant_id = self.kwargs.get('product_variant_id')

            player = context['product'].nba_player
            team = context['product'].team_id
            cart_product_form = CartAddProductForm(product_id=context['product'].id)

            context.update({
                'player': player,
                'team': team,
                'cart_product_form': cart_product_form,
                'is_out_of_stock': is_out_of_stock,
            })

            if product_variant_id:
                try:
                    product_variant = ProductVariant.objects.get(id=product_variant_id)
                    context['product_variant'] = product_variant
                except ProductVariant.DoesNotExist:
                    pass

            return context