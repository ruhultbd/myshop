from django.shortcuts import render
from django.views import View
from home.models import Banner
from product.models import Product

class HomeView(View):
    def get(self, request):
        trendingProducts = Product.objects.filter(tag='Trending').order_by('-id')[:5]
        feturedProducts = Product.objects.filter(tag='Featured').order_by('-id')[:5]
        newProducts = Product.objects.filter(tag='New Arrival').order_by('-id')[:5]
        saleProducts = Product.objects.filter(tag='On Sale').order_by('-id')[:5]

        context = {'title': 'Home'}
        context['banners']          = Banner.objects.order_by('ordering')
        context['trendingProducts'] = trendingProducts
        context['feturedProducts']  = feturedProducts
        context['newProducts']      = newProducts
        context['saleProducts']     = saleProducts

        return render(request, 'home/index.html', context)
