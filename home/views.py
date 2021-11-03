from django.shortcuts import render
from django.views import View
from home.models import Banner

class HomeView(View):
    def get(self, request):
        context = {'title': 'Home'}
        context['banners'] = Banner.objects.order_by('ordering')
        return render(request, 'home/index.html', context)
