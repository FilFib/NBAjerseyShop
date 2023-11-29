from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import *
from cart.forms import CartAddProductForm



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

    def get(self, request, *args, **kwargs):       
        product_id = self.kwargs['pk']
        product_variant_id = request.GET.get('product_variant_id')
        product_variant = get_object_or_404(ProductVariant, id=product_variant_id, product_id=product_id)
        product = Product.objects.all()
        # image = product.image
        # price = product.price
        # description = product.description
        # player= product.nba_player
        # team = product.team_id
        cart_product_form = CartAddProductForm(product_id=product_id)

        # context = {
        #         'price': price,
        #         'description': description,
        #         'player': player,
        #         'image': image,
        #         'team': team,
        #         'cart_product_form': cart_product_form,
        # }
        return render(request, 'detail_product.html', {'product':product, 'product_variant': product_variant, 'cart_product_form': cart_product_form})

