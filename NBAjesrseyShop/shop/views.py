from django.shortcuts import render, get_object_or_404
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


class ProductDetailView(View):
    model = Product
    template_name = 'detail_product.html'
    context_object_name = 'detail'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Product.objects.filter(id=product_id)

    def get(self, request, pk, is_out_of_stock=False, product_variant_id=None):
        is_out_of_stock = bool(is_out_of_stock)
        product = Product.objects.get(pk=pk)
        player = product.nba_player
        team = product.team_id
        cart_product_form = CartAddProductForm(product_id=product.id)
        context = {
                'product': product,
                'player': player,
                'team': team,
                'cart_product_form': cart_product_form,
                'is_out_of_stock': is_out_of_stock,}
        if product_variant_id:
            product_variant = ProductVariant.objects.get(id=product_variant_id)
            context['product_variant'] = product_variant
        return render(request, 'detail_product.html', context)