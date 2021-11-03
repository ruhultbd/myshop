from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        context = {'title': 'Home'}
        context['banners'] = {}
        return render(request, 'home/index.html', context)
