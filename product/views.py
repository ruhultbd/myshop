# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import product
from product.models import Category


class ListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {'title': 'Products', 'page_title': 'Product List'}
        return render(request, 'product/index.html', context)


class CategoryListView(LoginRequiredMixin, View):
    def get(self, request, id=False):
        categories = Category.objects.order_by('-id')
        parentCategories = Category.objects.filter(status='Active', parent=0).order_by('-id')

        context = {'title': 'Categories', 'page_title': 'Product Categories', 'categories': categories, 'parentCategories':parentCategories}

        context['single_category'] = False
        if id:
            context['category_id'] = id
            context['single_category'] = get_object_or_404(Category, pk=id)

        return render(request, 'product/category/index.html', context)

    def post(self, request):
        categoryName = request.POST['name'].strip()
        parentCat = 0
        errorMessage = None

        if (not categoryName):
             errorMessage = 'Category Name is required.'
        elif len(categoryName) < 4:
             errorMessage = 'Category Name is required.'

        if not errorMessage:
             newCategory = Category(name=categoryName, parent=parentCat)
             newCategory.save()
             messages.add_message(request, messages.SUCCESS, 'New category Successfully added')
        else:
            messages.add_message(request, messages.WARNING, errorMessage)
        return redirect('/product/categories')
