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

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        player= product.nba_player
        team = product.team_id
        product_variants = ProductVariant.objects.filter(product_id=pk)
        cart_product_form = CartAddProductForm(product_variants)
        
        context = {
                'product': product,
                'player': player,
                'team': team,
                'cart_product_form': cart_product_form,
        }
        return render(request, 'detail_product.html', context)



    # def get(self, request, pk):
    #     product_id = self.kwargs['pk']
    #     product = Product.objects.get(pk=pk)
    #     player = product.nba_player
    #     team = product.team_id
    #     # product_variants = ProductVariant.objects.filter(product_id=product_id)
    #     # cart_product_form = CartAddProductForm(product_variants)
        
    #     context = {
    #         'product': product,
    #         'player': player,
    #         'team': team,
    #     }
    #     return render(request, 'detail_product.html', context)

    # def post(self, request, pk):
    #     product_id = self.kwargs['pk']
    #     product_variants = ProductVariant.objects.filter(product_id=pk)
    #     cart_product_form = CartAddProductForm(request.POST)
    #     cart_product_form.fields['size'].choices = [(variant.size, variant.size) for variant in product_variants]

    #     if cart_product_form.is_valid():
    #         selected_size = cart_product_form.cleaned_data['size']
    #         product_variant = ProductVariant.objects.get(product_id=product_id, size=selected_size)
    #         request.session['product_variant_id'] = product_variant.id
    #         return render(request, 'detail_product.html', {'product_variant': product_variant})

    #     context = {
    #         'product_variants': product_variants,
    #         'cart_product_form': cart_product_form,
    #     }
    #     return render(request, 'detail_product.html', context)




    # def get(self, request, pk):       
    #     product_id = self.kwargs['pk']
    #     product = Product.objects.get(pk=pk)
    #     player = product.nba_player
    #     team = product.team_id
    #     product_variants = ProductVariant.objects.filter(product_id=product_id)
    #     cart_product_form = CartAddProductForm()
    #     cart_product_form.fields['size'].choices = [(variant.size, variant.size) for variant in product_variants]

    #     context = {
    #             'product': product,
    #             'player': player,
    #             'team': team,
    #             'cart_product_form': cart_product_form,
    #     }
    #     return render(request, 'detail_product.html', context)

    # def post(self, request, pk):
    #     product_id = self.kwargs['pk']
    #     product_variants = ProductVariant.objects.filter(product_id=pk)
    #     cart_product_form = CartAddProductForm(request.POST, product_id=pk)
    #     cart_product_form.fields['size'].choices = [(variant.size, variant.size) for variant in product_variants]

    #     if cart_product_form.is_valid():
    #         selected_size = cart_product_form.cleaned_data['size']
    #         product_variant = ProductVariant.objects.get(product_id=pk, size=selected_size)
    #         cart_product_form.cleaned_data['product_variant_id'] = product_variant.id
    #         return render(request, 'detail_product.html', {'product_variant':product_variant} )
        

    # def get(self, request, pk):       
    #     product_id = self.kwargs['pk']
    #     product = Product.objects.get(pk=pk)
    #     player= product.nba_player
    #     team = product.team_id
    #     cart_product_form = CartAddProductForm(product_id=product_id)
    #     context = {
    #             'product': product,
    #             'player': player,
    #             'team': team,
    #             'cart_product_form': cart_product_form,
    #     }
    #     return render(request, 'detail_product.html', context)