from django.urls import path
from .views import ListView, CategoryListView

from . import views

urlpatterns = [
    path('', ListView.as_view(), name="products"),
    path('categories', CategoryListView.as_view(), name="product-categories"),
    path('category/<int:id>', CategoryListView.as_view(), name="category.edit"),

]
